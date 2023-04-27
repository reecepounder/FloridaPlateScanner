_This repository is archived and will no longer be maintained. If you wish to update or edit the code please fork._

# Florida License Plate Bruteforcer

Python script that will bruteforce available plates in the Florida DMV for a set length of characters (excludes numbers)
More info on my blog: [click](https://pounder.dev)


Usage:
```python
import dmv_check
# Check for all 3 letter permutations and make a file with the results
dmv_check.check()

# ... or you can use the returnValues parameter to return the results as a list instead
availablePlates = dmv_check(3,returnValues=True)
print(availablePlates)

# ... You can also toggle output to console (defaults to __debug__ unless overridden).
dmv_check(3, printDebugStatements=False)
```


!! DISCLAIMER !!
This tool should only be used with permission from the party(parties) responsible for the ownership and control of the subject server.
It makes repetitive, fast-paced web requests which could be considered attempts to Denial of Service attack the system. Add a delay if you're
concerned about this, and can leave it running all night long. No warranty is provided, nor do I maintain responsibility for what you do.
