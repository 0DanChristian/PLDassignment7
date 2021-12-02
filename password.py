# password validator
# password must be greater than 15 letters
# password must have at least one number
# password must have atleast one special char (!@#$%^&*(()_+ etc
# example input P@ssw0rd+P@ssw0rd ===== valid

# introduction
print("\n\033[0;37;45mWelcome!\033[0m\n")
# ask for user
user = input("\nPlease enter your \033[1mname\033[0m: ")
# welcome
print(f"\n\033[1;36;47mWelcome {user}\033[0m!, this program will validate if your password is valid! \n")

# import
import re

# define
def validate_password():
          password= input("Enter your desired password: ")
          print(f"\nYour password \033[3;32;40m{password}\033[0m")
          valid = True 
          while valid:  
                # if password is less than 15 characters
              if len(password) <= 15: 
                  print("\n\033[0;37;41mPassword must have 15 characters\033[0m")     
                  break
                # if pasword doesn't contain numbers
              elif not re.search("[0-9]",password): 
                  print("\n\033[0;37;41mPassword must have atleast one number\033[0m")
                  break
                # if password doesn't contain upper case letter
              elif not re.search("[A-Z]",password): 
                  print("\n\033[0;37;41mPassword must have atleast one uppercase\033[0m")
                  break
                # if password doesn't contain special character
              elif not re.search("[`~!@#$%^&*()-_=+[]|;:,<.>/?]",password): 
                  print("\n\033[0;37;41mPassword must have atleast one special character\033[0m")
                  break
                # if contains blank space
              elif re.search("\s",password): 
                  print("\n\033[0;33;40mYou cannot have blank spaces in your password...\033[0m")
                  break
                # Valid password has been created
              else:
                  print("\n\033[032;40mValid:>\033[0m\n")
                  valid = False 
                  break
                # invalid
          if valid:
              print("\n\033[0;37;41mThe password you input is invalid\033[0m\n")
              validate_password()

validate_password()