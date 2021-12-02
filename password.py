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

# import
import re

def validate_password():
          password= input("Enter your desired password: ")
          valid = True 
          while valid:  
                #if password is less than 15 characters
              if len(password) <= 15: 
                  print("Password length must be 15 characters")     
                  break
                #if pasword doesn't contain numbers
              elif not re.search("[0-9]",password): 
                  print("You need at least one number")
                  break
                #if password doesn't contain upper case letter
              elif not re.search("[A-Z]",password): 
                  print("You need at least one upper case character")
                  break
                #if password doesn't contain special character
              elif not re.search("[$#@]",password): 
                  print("You need at least one special character please")
                  break
                #if contains blank space
              elif re.search("\s",password): 
                  print("You cannot have blank spaces in your password...")
                  break
                #Valid password has been created
              else:
                  print("Valid Password")
                  valid = False 
                  break

          if valid:
              print("Not a Valid Password")
              validate_password()

validate_password()