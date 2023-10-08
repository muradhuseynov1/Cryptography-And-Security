# TASK: Caesar Encryption and Decryption

def encrypt(plain,key):
    cipher="" # cipher is an empty string where the encrypted data will be stored
    # traverse the plain text
    for i in range(len(plain)): 
        char=plain[i] # for loop will go through each character of the entered plain text and store them in the variable char
        # Encrypt uppercase characters in plain text
        if(char.isupper()):
            cipher += chr((ord(char) + key - 65) % 26 + 65) # ord function will give the ASCII value of character and we decrease 65 because the first uppercase letter's ASCII code is 65 and we take modulo 26 as there 26 letter in English alphabet and when we add key to the characters, the sum might be more than 26
        # Encrypt lowercase characters in plain text
        else:
            cipher += chr((ord(char) + key - 97) % 26 + 97) # same with uppercase, we only decrease by 97 not 65, as the first lowercase letter's ASCII code 97
    return cipher # returning the encrypted text

def decrypt(plain,key):
    cipher=""
    # traverse the plain text
    for i in range(len(plain)): # for
        char=plain[i]
        # Decrypt uppercase characters in plain text
        if(char.isupper()):
            cipher += chr((ord(char) - key - 65) % 26 + 65) # in order to decrypte the encrypted text, we have to go back by the same number of "key"s by substracting the key, as we hava encryted to text by going key number further in the alphabet in each character
        # Decrypt lowercase characters in plain text
        else:
            cipher += chr((ord(char) - key - 97) % 26 + 97) 
    return cipher

plainText = input("Enter plain text: ")
key = int(input("Enter key: "))
print("The original message: ", plainText)
print("The encrypted message: ", encrypt(plainText, key))
print("The decrypted message: ", decrypt(encrypt(plainText, key), key))