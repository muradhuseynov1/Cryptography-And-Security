# TASK:
# Alice uses a simple xor encryption (where C = M xor K)
# For the key, she uses the str(random()[2:], with a seed that is NOT truly random.
# She uses the current date along with a space and the current hour as its seed.Here are a few examples of the seed value: "2022-01-22 09" and "2022-11-21 19".
# Bob intercepts and got the following ciphertext in hexa ‘4c5c4117525f475e52195a4d’.
# Assume that Bob knows the above information. Additionally he know that Alice encrypted the message on 2022 February 10, possibly from 10 up to 18.

import random

cipher_hex="4c5c4117525f475e52195a4d"
plainText=bytearray.fromhex(cipher_hex).decode('utf-8')

def xor(string1, string2):
    return "".join([chr(ord(c1) ^ ord(c2)) for (c1, c2) in zip(string1, string2)])

for i in range(10, 18+1):
    random.seed( '2022-02-10 ' + str(i) )
    k = str(random.random())[2:]
    print("[%d]: %s" %(i,xor(plainText, k)))