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
print(f"\nWelcome \033[0;30;47m{user}\033[0m!, this program will validate if your password is valid! \n")

upper, special, digit = 0, 0, 0
password = input("Enter your password: ")
if (len(password) >= 15):
    for i in password:
        for word in password.split():
            if(word[0].isupper()):
                upper += 1
        if(i.isdigit()):
            digit += 1
        if(i == '@' or i == '$' or i == '_' or i == '#'):
            special += 1
else:
    print("Password must be greater than 15 letters")
if (upper >= 1 and special >= 1 and digit >= 1):
    print("Valid Password")
else:
    print("Invalid Password")