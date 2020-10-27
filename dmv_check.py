from itertools import product
import requests, time, json

def check(letters = 3):
  print(   '------- FLORIDA DMV BRUTEFORCER -------')
  print(   '    Get the license plate you wanted   ')
  print(   '       without the imagination!        ')
  print()
  print("Warning: This will overwrite existing data.")
  print("Warning: If HTTP != 200, stop! and report on GitHub")
  print()
  t0 = time.time()

  arr = list(map("".join, product('ABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=letters)))
  print("Testing " + str(letters) + "-letter combinations. " + str(len(arr)) + ' values to test. This will take a while...')
  use = []
  available = []



  chunk_size = 5
  for i in range(0, len(arr), chunk_size):
      chunk = arr[i:i+chunk_size]
      use.append(chunk)

  i = 0
  j = 0

  for x in use:
    if len(x) == 5:
      j+=5
      # I'm concerned about the security implications of leaving these base64-encoded values in the source code. So, in an effort to censor them, I have replaced my copy with one I made in a VM while on a VPN. If you find that this can be reversed to vulnerable information, please contact me ASAP
      val = {
        '__VIEWSTATE' : '/wEPDwULLTE2Nzg2NjE0NDhkZOho2qa4uYR/f+8obq3/ImCxcNxH36xm67bHA/DCf7mQ',
        '__VIEWSTATEGENERATOR' : '0719FE0A',
        '__EVENTVALIDATION'    : '/wEdAAhSwalmR41pxSO86DbjFtdTphigSR1TLsx/PgGne7pkTpB7LNiAmBrY+lkV4yRhukq4UDQtuzi2yL5oIR7b2qk2FOSIJTkYpiT1a4/KG6JIzmxkUFM1z5DWUKiTRJ9g63z4IcjYoaGuA6R78NuEHgsNxxpsutNlt3RySqFY6uFDYws1JyvmrlwnteHbS5dhyF7dKCjfIe8P3vD5UreH3OSv',
      
        'ctl00$MainContent$txtInputRowOne'  : x[0],
        'ctl00$MainContent$txtInputRowTwo'  : x[1],
        'ctl00$MainContent$txtInputRowThree': x[2],
        'ctl00$MainContent$txtInputRowFour' : x[3],
        'ctl00$MainContent$txtInputRowFive' : x[4],
        'ctl00$MainContent$btnSubmit'       : 'Submit'}

      r = requests.post('https://services.flhsmv.gov/mvcheckpersonalplate/', data=val)

      # note: idk why but the programmers put 'OutPut' for 1 and 2, and 'Output' for 3 4 and 5.
      if '<span id="MainContent_lblOutPutRowOne" class="outputText" style="color: #0000a0; font-weight: bold">AVAILABLE</span>' in r.text:
        available.append(x[0])
        i+=1  
          
      if '<span id="MainContent_lblOutPutRowTwo" class="outputText" style="color: #0000a0; font-weight: bold">AVAILABLE</span>' in r.text:
        available.append(x[1])
        i+=1  
              
      if '<span id="MainContent_lblOutputRowThree" class="outputText" style="color: #0000a0; font-weight: bold">AVAILABLE</span>' in r.text:
        available.append(x[2])
        i+=1  
          
      if '<span id="MainContent_lblOutputRowFour" class="outputText" style="color: #0000a0; font-weight: bold">AVAILABLE</span>' in r.text:
        available.append(x[3])
        i+=1  
          
      if '<span id="MainContent_lblOutputRowFive" class="outputText" style="color: #0000a0; font-weight: bold">AVAILABLE</span>' in r.text:
        available.append(x[4])
        i+=1

      print("Currently at " + str(i) + " found, " + str(j) + " tried. HTTP " + str(r.status_code))
    else:
      print("Values remaining is less than 5. Execute manually.")

  print("\n------- DONE! Took " + str("%.2f" % (time.time() - t0)) + " seconds -------")
  print(str(len(arr)) + ' values tried, ' + str(i) + ' available. Saved to file "letters.json"')
  
  f = open("letters.json", "w")
  f.write(json.dumps(available))
  f.close()
