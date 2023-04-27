""" 
FLORIDA DMV BRUTEFORCER

This script generates and tests letter permutations to check the availability of license plates in the Florida DMV website. It sends HTTP requests to the website and parses the HTML response to find available values.

Usage:
- Call the check() function with no arguments to test all 3-letter combinations.
- Call the check(letters=n) function with n as the number of letters in the combinations to test. Results will be saved to a file named n_letters_0000.json, where 0000 is the current epoch time.
- Call the check(letters=n, returnValues=True) function to get a list of available values instead of saving them to a file.
- Call the check(letters=n, printDebugStatements=False) function to disable progress information from being printed to the console. It will default to the state of __debug__ if unset.


Author: Reece Pounder

"""

from itertools import product
import requests, time, json

# Required form data values. Not a clue what they're for.
formValuesOriginal = {
    '__VIEWSTATE':
    '/wEPDwULLTE2Nzg2NjE0NDhkZOho2qa4uYR/f+8obq3/ImCxcNxH36xm67bHA/DCf7mQ',
    '__VIEWSTATEGENERATOR': '0719FE0A',
    '__EVENTVALIDATION':
    '/wEdAAhSwalmR41pxSO86DbjFtdTphigSR1TLsx/PgGne7pkTpB7LNiAmBrY+lkV4yRhukq4UDQtuzi2yL5oIR7b2qk2FOSIJTkYpiT1a4/KG6JIzmxkUFM1z5DWUKiTRJ9g63z4IcjYoaGuA6R78NuEHgsNxxpsutNlt3RySqFY6uFDYws1JyvmrlwnteHbS5dhyF7dKCjfIe8P3vD5UreH3OSv',
    'ctl00$MainContent$btnSubmit': 'Submit'
}


def check(letters=3, *, returnValues=False, printDebugStatements=__debug__):
    """
    This function tests all possible combinations of letters and numbers for license plates of length 'letters'.
    
    Args:
        letters (int, optional): The number of letters in each license plate. Defaults to 3.
        returnValues (bool, optional): If True, the function returns a list of available license plates. If False, the function saves the list to a file. Defaults to False.
        printDebugStatements (bool, optional): If True, prints debug information while running. Defaults to the state of __debug__.
        
    Returns:
        list or None: If returnValues is True, returns a list of available license plates. Otherwise, returns None.
    """
    if printDebugStatements:
        print('------- FLORIDA DMV BRUTEFORCER -------')
        print('    Get the license plate you wanted   ')
        print('       without the imagination!        ')
        print()
        print()

    t0 = time.time()
    arr = list(
        map("".join,
            product('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', repeat=letters)))
    if printDebugStatements:
        print("Testing " + str(letters) + "-letter combinations. " +
              str(len(arr)) + ' values to test. This will take a while...')

    # For testing, uncomment this line to reduce the number of permutations that are tested
    #arr = ['BABAF' + str(i) for i in range(3, 11)]

    use = []
    available = []

    # Chop the permutations into chunks of 5, because DMV only accepts 5 at a time.
    max_chunk_size = 5
    for i in range(0, len(arr), max_chunk_size):
        chunk = arr[i:i + max_chunk_size]
        use.append(chunk)

    # Number of tried permutations
    tested = 0

    # Iterate permutations to use
    for x in use:
        formValues = formValuesOriginal.copy()
        correlation = ["", "One", "Two", "Three", "Four", "Five"]
        numsEntered = []

        # For every permutation, add it as a key
        for i, value in enumerate(x, start=1):
            key = f'ctl00$MainContent$txtInputRow{correlation[i]}'
            formValues[key] = value
            numsEntered.append(value)

        # Make request
        r = requests.post('https://services.flhsmv.gov/mvcheckpersonalplate/',
                          data=formValues)

        # For every response that is indicated as available, add the corresponding value to the available values list
        for i, value in enumerate(x):
            if f'{correlation[i+1]}" class="outputText" style="color: #0000a0; font-weight: bold">AVAILABLE</span>' in r.text:
                available.append(numsEntered[i])

        # Prints some debug info for when used in a graphical terminal
        tested += len(numsEntered)
        if printDebugStatements:
            print(str(len(available)), "found,", str(tested), "tried.")

    if printDebugStatements:
        print("\n------- DONE! Took " + str("%.2f" % (time.time() - t0)) +
              " seconds -------")
        print(
            str(len(arr)) + ' values tried, ' + str(len(available)) +
            ' available.')

    if not returnValues:
        f = open(str(letters) + "_letters_" + str(time.time()) + ".json", "w")
        f.write(json.dumps(available))
        f.close()
        if printDebugStatements:
            print("Saved to file letters.json successfully.")
    else:
        if printDebugStatements:
            print("Completed successfully. Returning...")
        return available
