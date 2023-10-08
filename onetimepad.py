# TASK: Write a code to perform an encryption and decryption using one-time-pad.

import string

LETTERS = string.ascii_letters  # this string function will concatenate all lowercase and uppercase letters and put
                                # in the variable called LETTERS

def encrypt(plaintext, key):
    cipher = ""  # cipher is the variable which will contain the encryted data, initially it is an empty string

    for i in range(len(plaintext)): # the for loop start from 0 and goes till the length of the plain text, it is used to read the characters of the plain text
        char = plaintext[i]  # in each iteration of the loop, the i-th value/character will be stored in this variable
        k = LETTERS.find(key[i])  # the string find() function will help to find the index of each character that occured the first in the text

        if char.isupper(): # encrytion of uppercase character
            cipher += chr((ord(char) + k - 65) % 26 + 65)  # in order to encrytp a character, it should be key letter forwarded in the alphabet by adding key to the character's ASCII value. For this we use ord() function.
            # also we have to substract 65 because it is the ASCII code of the first lowercase character. We find module 26 becuase the English alphabet consists of 26 letters and in case when we add key and it exceeds 26, it should go back to the first letter so we module 26 and add 65 as it is the ASCII value of the first character.
        else:
            cipher += chr((ord(char) + k - 97) % 26 + 97)  # same applies to the lowercase, with a small difference: instead of 65, we use 97 in the equation, as 97 is the ASCII value of the first uppercase letter
    return cipher  # return the encrypted text


def decrypt(plaintext, key):
    cipher = ""  

    for i in range(len(plaintext)):
        char = plaintext[i]  
        k = LETTERS.find(key[i]) 

        if char.isupper():
            cipher += chr((ord(char) - k - 65) % 26 + 65)  

        else:
            cipher += chr((ord(char) - k - 97) % 26 + 97)  
    return cipher  
    # it is almost the same for the decryption. We only substract key from the ASCII values of the characters. In encryption we added key because we encrypt by going key value forward in the alphabet. So, for decryption we have to go back key value back in the alphabet to its original positon


plainText = input("Enter the plain input text: ")
key = str(input("Enter the key(it must be string and the chracter number should be equal to the character number of the plain text): "))
print("The encryption of the plain text:", encrypt(plainText, key))
print("The decryption of the encrypted plain text:", decrypt(encrypt(plainText, key), key))