# TASK:
# Write python code that does a brute force attack against Caesar encryption.
# Import a  textfile containing a few thousand common English words in your code.
# Create a program that takes in an encrypted string as input (or simply store it in a variable), then try decoding various messages of ALL possibilities (Perform the brute-force attack)
# Use the dictionary of common English words that you have imported into your code to try to automatically determine which shift is most likely be a valid plaintext.
# Your code should only output the decrypted string if it found it in the common English words.

def decrypt(plain,key):
    cipher = ""
    # traverse the plain text
    for i in range(len(plain)): # for
        char = plain[i]
        # Decrypt uppercase characters in plain text
        if(char.isupper()):
            cipher += chr((ord(char) - key - 65) % 26 + 65) # in order to decrypt a character, it should be key letter backwared in the 
                                                            # alphabet by substracting key from the character's ASCII value. For this we use ord() function.
                                                            # also we have to substract 65 because it is the ASCII code of the first lowercase character. 
                                                            # We find module 26 becuase the English alphabet consists of 26 letters and in case when we substract key and it is out of 26 letter interval, 
                                                            # it should go back to the first letter so we module 26 and add 65 as it is the ASCII value of the first character.
        # Decrypt lowercase characters in plain text
        else:
            cipher += chr((ord(char) - key - 97) % 26 + 97) # same applies to the lowercase, with a small difference: 
                                                            # instead of 65, we use 97 in the equation, as 97 is the ASCII value of the first uppercase letter
    return cipher

encrypted = input("Encrypted word: ").lower() # taking the encrypted text from the input console
listOfWords = [] # dictonary: we take words from words.txt file. Initially, we have an empty list which will contain words later
for word in open("words.txt", "r"):  # the for loop will open the words.txt file and read it using 'r', r stands for read, using file handling operations
    listOfWords.append(word.strip().lower())  # append function adds elements to the list. We use strip() and lower() functions to guarantee that there's no extra space and they're all lower case, respectively

key = 0 ; existsWord = False  # initially, as unit values, we set key to 0 and we have a boolean value which indicates whether we have found the word or not and it is set to false         
while (key < 27) and (not existsWord):  # the while loop have the iterations based on two conditions: while the key is less than 27 as there're 26 letters only in the English alphabet and while there's no word found/exists, which is the declared boolean value
    decrypted = decrypt(encrypted, key)  # decrypting the encrypted entered value
    if decrypted in listOfWords:   # if statement will operate in case the decrypted text is in the list of words
        existsWord = True   # if the decrypted text or word is in the list of words, we set the boolean value to true
        print("decrypted text: %s and it's key: %d" % (decrypted, key)) # using placeholders in the print function: displaying the key and the decrypted word which is in the list of words
    else:
        key = key+1 # if the decrypted word is not in the list of words, we increment the key and use it for decryption to check whether the new decrypted word is in the list of words or not

if not existsWord:
    print("The encrypted message was decrypted using all the keys, but wasn't found in the list of words!") # line 33 and 34 will work only if 26 keys used for decryption and the decrypted words was not in the given list of words
                                                                                                           # it will simply output an error message 