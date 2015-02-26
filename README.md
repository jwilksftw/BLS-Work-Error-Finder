# BLS-Work-Error-Finder
Before I created this program, analysts working on the Occupational Outlook Handbook (http://www.bls.gov/ooh/) had
to search for errors (incorrect data, incorrect or missing boilerplate language, language not match the 
BLS style guide) manually. This took a tremendous amount of time, given the 334 occupatinal profiles, 
and resulted in an error checklist that had well over 80 items on it. Due to the size of the checklist, 
errors would be missed as there was too much for a human to check. This program was able to eliminate 
approximately 50 of the items on said checklist.

The system of programs used to check for errors first employs oohlivechecker.py to pull the most recent text from 
bls.gov/ooh. The text is placed in respective files to match each profile. Then, oohlivehandsearch.py is used
to find the actual errors. The user inputs the text or phrases they are looking for on line 26 with. 
Regular expressions can be used in this search. Also, if the user is looking for cases in which expected
text is missing, they can use line 91 to enter in the word or phrase they are searching for.
