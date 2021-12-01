# program to count vowel or consonant of the given word or sentence

# introduction
print("\n\033[0;37;45mWelcome!\033[0m")
# ask for use
user = input("\nPlease enter your \033[1mname\033[0m: ")
# again, welcome
print(f"\nWelcome \033[0;30;47m{user}\033[0m!, in this program you can enter a word or a senctence and we'll count how many \033[0;32;47mwords\033[0m, \033[0;32;47mvowels\033[0m and \033[0;32;47mconsonant\033[0m there is!\n")

str=input("\nPlease enter a word or a sentence!: ")

# wordcount, vowels and consonant
vowels = 0
consonants = 0
wordcount = 1

# call the lower function to avoid upper case letter
str.lower() 
for i in str:
    if(i == 'a'or i == 'e'or i == 'i'or i == 'o'or i == 'u' ):
           vowels=vowels + 1
    elif i in ' ':
        wordcount += 1
    else:
        consonants=consonants + 1

# display
print("\nThe number of \033[0;32;47mwords\033[0m in the given input is",wordcount, end='')
print(", the number of \033[0;32;47mvowel/s\033[0m is",vowels, end='')
print(" and the number of \033[0;32;47mconsonant/s\033[0m is",consonants,)

print("\n\033[0;37;42mVowel/s\033[0m       : ", vowels)
print("\033[0;37;42mConsonant/s\033[0m   : ", consonants)
print("\033[0;37;42mWordcount\033[0m     : ", wordcount)

# end of program
print(f"\nThank you \033[0;37;46m{user}\033[0m, u stup*d piece of shi*!\n")