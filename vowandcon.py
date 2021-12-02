# program to count vowel or consonant of the given word or sentence

# introduction
print("\n\033[0;37;45mWelcome!\033[0m")
# ask for use
user = input("\nPlease enter your \033[1mname\033[0m: ")
# again, welcome
print(f"\nWelcome \033[0;30;47m{user}\033[0m!, in this program you can enter a word or a senctence and we'll count how many \033[0;32;47mwords\033[0m, \033[0;32;47mvowels\033[0m and \033[0;32;47mconsonant\033[0m there is!\n")

inUser = input("\nPlease enter a word or a sentence!: ")

# wordcount, vowels and consonant
vowels = 0
consonants = 0
wordcount = 0

# call the lower function to avoid upper case letter
inUser.lower() 
for word in inUser:
    if word.upper() in "AEIOU" :
           vowels += 1
           wordcount += 1
    elif word.upper() in "BCDFGHJKLMNPQRXTVWXYZ":
        consonants += 1
        
wordcount = inUser.split()

# print what was input
print(f"\n\033[3;36;40m{inUser}\033[0m")    
# display
print("\n\033[0;32;40mWord/s\033[0m     : ", len(wordcount), "\n\033[0;32;40mVowel/s\033[0m    : ", vowels, "\n\033[0;32;40mConsonant/s\033[0m: ", consonants)

# end of program
print(f"\n\033[1;32;45mThank you {user}!\033[0m\n")