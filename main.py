import dmv_check
# Check for all 3 letter permutations and make a file with the results
dmv_check.check()

# ... or you can use the returnValues parameter to return the results as a list instead
#availablePlates = dmv_check(3, returnValues=True)
#print(availablePlates)

# ... You can also toggle output to console (defaults to __debug__ unless overridden).
#dmv_check(3, printDebugStatements=False)
