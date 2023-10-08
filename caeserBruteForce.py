# TASK: Caesar Brute force attack

# import string will add all the string functions to the file
import string 

ciphertext = "JYFWVNYHWOF" # this the cipher text, the text that needs to be coverted to the plain/readable form
LETTERS = string.ascii_uppercase # ascii_uppercase is a string function that concatenates all the uppercase letter and puts these character into the variable LETTER

for key in range(len(LETTERS)):
    translated = ""     # translated is the variable that will contain the decrypted/converted text. Initially it's an empty string
    for symbol in ciphertext:   # the for loop will go through each character of the ciphertext
        if symbol in LETTERS:   # if statement will check if there is an uppercase character
            num = LETTERS.find(symbol)    # find() is a string function that finds the index of a character apperared the first in the string. 
                                          # So we will find the indexes of the characters in the ciphertext and store them in the variable num
            num = num - key    # we substract key from this number as we want to convert it into plain form so we need to go back key value in the alphabet
            if num < 0:    # if statement will check if the result of the substraction is negative or not 
                num = num + len(LETTERS) # for negative results we have to add the number of uppercase letters to the value we got, because we are dealing only with uppercase characters
            translated = translated + LETTERS[num] # we fill in the empty string by the converted uppercase letters, according to the indexes
        else:    # when the characters of the ciphertext are not uppercase letters:
                translated = translated + symbol    # we simply fill in the empty string with the characters of the ciphertext
    print('Hacking key #%s: %s' % (key,translated)) # using placeholders in the print function to output the keys and the converted texts