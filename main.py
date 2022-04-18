import re

password = input("Type your password:")
k = 0

if (len(password)<14):
    print("Password must consist at least 14 characters.")
    
if not re.search("[a-z]", password):
        print("Password must consist lower case symbols")
        
if not re.search("[A-Z]", password):
        print("Password must consist upper case symbols")
        
if not re.search("[0-9]", password):
        print("Password must consist digits")
        
if not re.search("[!?_@$]", password):
        print("Password must consist punctuation numbers")
else:
        print("Strong Password")
    



