# n=(247) e = (7) <----> The public key that was assigned to me by my professor.

from pydoc import plain
import secrets
from sympy import randprime
from math import gcd

# ------------------------------------------------------------------------------------
# Necessary functions: 
# extended greatest common dinominator
def egcd(a, b):
    if a == 0:
        return(b,0,1)
    else:
        g, x, y = egcd(b%a,a)
        return (g, y- (b//a)*x,x)

# modular multiplicative inverse
def modinv(b,n):
    g,x, _ = egcd(b,n)
    if g == 1:
        return x % n

# ------------------------------------------------------------------------------------

# largest_prime_factor function is used to find two prime numbers which their product result in the RSA modulus
# it goes thourgh every number between 1 and the given number and checks if number is prime and divisible by the given number and if the conditions are met,
# it will iterate the next number until it finds the last good number which is the greatest one 
def largest_prime_factor(n):
    return next(n // i for i in range(1, n) if n % i == 0 and is_prime(n // i))
def is_prime(m):
    return all(m % i for i in range(2, m - 1))

# ------------------------------------------------------------------------------------

rsa_modulus = 247

prime1 = largest_prime_factor(rsa_modulus)
prime2 = int(247/prime1) # we find the second prime number by dividing the RSA_modulus by the first prime number


# totient of a prime number is equal to the number of all number from 1 to (n-1). 
# As the rsa module 247
# equals to the product of two prime numbers, we can find the totient of the prime numbers separately and multiply them in order to find
# the totient of rsa modulo
totient = (prime1-1) * (prime2-1)


public_exponent = 7 # Parameter e
private_exponent = modinv(public_exponent, totient) # Parameter d

plaintext = 'My name is Murad and I study at ELTE'

# Encryption function taken from the slides
def rsa_encrypt(plaintext, rsa_modulus, public_exponent):
    cipher = ''.join(chr((ord(ch)**public_exponent) % rsa_modulus)for ch in plaintext)
    return cipher.encode().hex()

# Decrytion function taken from the slides 
def rsa_decrypt(cipher_text, rsa_modulus, private_exponent):
    return ''.join(chr((ord(ch)**private_exponent) % rsa_modulus)for ch in bytearray.fromhex(cipher_text).decode())


encrypted_plain = rsa_encrypt(plaintext,rsa_modulus,public_exponent) # encryting the plain text --> cipher 
decrypted_cipher = rsa_decrypt(encrypted_plain,rsa_modulus,private_exponent) # decrytping the cipher --> plain text


# ---------------------------------------------------------------------------------------- printing 
print("RSA public key: (RSA modulus n: " + str(rsa_modulus) + " , public exponent e: " + str(public_exponent) + ")") # public key
print("(RSA modulus: " + str(rsa_modulus) + ") = (primeNumber1: " + str(prime1) + ") x (primeNumber2: " + str(prime2) + ")") # printing prime1 and prime 2
print("Totient (phi function) of RSA modulus: " + str(totient)) # totient of the rsa modulo
print("Plain text: " + plaintext +"\n" + "Encryted plain text: " + encrypted_plain + "\n" + "Decrypted ciphered text: " + decrypted_cipher) # encrypt and decrypt