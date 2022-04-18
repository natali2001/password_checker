import re

password = input("Type your password:")
k = 0

if (len(password)<14):
    print("Password must be at least 14 characters long.")
    k = -1
    
if not re.search("[a-z]+[A-Z]", password):
        print("Password must contain both lowercase and uppercase characters")
        k = -1
        
if not re.search("[0-9]", password):
        print("Password must contain digits")
        k = -1
        
if not re.search("[!?_@$]", password):
        print("Password must contain at least one punctuation character")
        k = -1

if (k>-1):
    print('Strong Password')
    



