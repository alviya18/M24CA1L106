# Write a Python program to check the validity of password input by users.
#Validation:
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.

import re
password=input("Password ? :")
len=len(password)
pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@]).{6,16}$'
if re.match(pattern, password):
    print("Password is valid.")
else:
    print("Password is invalid.")


