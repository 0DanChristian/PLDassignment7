# password validator
# password must be greater than 15 letters
# password must have at least one number
# password must have atleast one special char (!@#$%^&*(()_+ etc
# example input P@ssw0rd+P@ssw0rd ===== valid

# introduction
print("\n\033[0;37;45mWelcome!\033[0m\n")
# ask for use
user = input("\nPlease enter your \033[1mname\033[0m: ")
# welcome
print(f"\nWelcome \033[0;37;46m{user}\033[0m!, this program will validate if your password is valid! \n")

# 
import re

# enter a password
password = input("Input your password: ")

# statement
x = True
while x:  
    if (len(password)<6 or len(password)>12):
        break
    elif not re.search("[a-z]",password):
        break
    elif not re.search("[0-15]",password):
        break
    elif not re.search("[A-Z]",password):
        break
    elif not re.search("[$#@]",password):
        break
    elif re.search("\s",password):
        break
    else:
        print("Valid Password")
        x=False
        break

if x:
    print("Not a Valid Password")