# # TASK:
# Write a full mini-aes encryption/decryption program that includes:
# - key addition procedure.
# - encryption and decryption procedure, including the inverse nibble substitution procedure.


# a nibble is four bits. 
# a block will be an array of four elements (a nibble each)
# this means that block = [nibble0, nibble2, nibble2, nibble3]

from base64 import decode
import binascii
from operator import xor
from pydoc import plain


#  -- Constant parameters -- #
nibble_size = 4  # bits
const_mix_column = ['0011','0010','0010','0011'] 
prime_modulus = '10011' # x^4 + x + 1
rcon = ['0001', '0010'] 
s_box = {'0000':'1110', '0001':'0100', '0010':'1101', '0011':'0001', '0100':'0010', '0101':'1111', '0110':'1011', '0111':'1000', '1000':'0011', '1001':'1010', '1010':'0110', '1011':'1100', '1100':'0101', '1101':'1001', '1110':'0000', '1111':'0111' }
s_box_inverse = {'0000':'1110', '0001':'0011', '0010':'0100', '0011':'1000', '0100':'0001', '0101':'1100', '0110':'1010', '0111':'1111', '1000':'0111', '1001':'1101', '1010':'1001', '1011':'0110', '1100':'1011', '1101':'0010', '1110':'0000', '1111':'0101'}
#  ------------------------ #


def mix_column(block):
    '''
    It performs the mix column step
    The input block will be multiplied by the fixed block 'const_mix_column' (modulu 'prime_modulus')
    '''
    res=[]
    for i in range(2):
        for j in range(2):
            n1 = p_mod_mul(const_mix_column[j], block[i*2], prime_modulus)
            n2 = p_mod_mul(const_mix_column[j+2], block[i*2 + 1], prime_modulus)
            res.append(bin(xor(int(n1, 2), int(n2, 2)))[2:].zfill(4))
    return res


def shift_row(block):
    '''
    It performs the shift row step.
    First nibble in the block does not shift. i.e. stays at the same place 
    Second nibble in the block will be shifted by one. i.e. Goes to the end of the block.
    Third block will be shifted by two. i.e. stays at the same place
    Fourth block will be shifted by three. i.e. Goes to the second place of the block.
    '''
    new_block = []
    new_block.append(block[0])
    new_block.append(block[3])
    new_block.append(block[2])
    new_block.append(block[1])
    return new_block

def nibble_sub(block):
    '''
    It performs the substitution based on the fixed s_box table 
    for each of the four nibbles in the input block.
    '''
    substitute = []
    for nibble in range(len(block)):
        substitute.append(s_box[block[nibble]])
    return substitute



def key_schedule(key):
    '''
    It performs the key schedule based on the fixed key schedule equations, 
    where the first block of the resulted key array is the same as the input key.
    '''
    key_blocks = []
    key_blocks.append ([key[i:i+4] for i in range(0, len(key), nibble_size)])
    for i in range(2):
        block = [bin(xor(xor(int(key_blocks[i][0], 2),int(s_box[key_blocks[i][3]], 2)), int(rcon[i], 2)))[2:].zfill(4)]
        block.append(bin(xor(int(key_blocks[i][1], 2), int(block[0], 2)))[2:].zfill(4))
        block.append(bin(xor(int(key_blocks[i][2], 2), int(block[1], 2)))[2:].zfill(4))
        block.append(bin(xor(int(key_blocks[i][3], 2), int(block[2], 2)))[2:].zfill(4))
        key_blocks.append(block)  
    return key_blocks


def key_addition(block, key):
    '''
    To do (1):
    It should perform the key addition part of the algorithm.
    The key addition is done by simple xor each of the 16 bits (that are divided into four nibbles)
    of the plain text with the 16 bits of the key.
    Both block and key are represented as a list of four binary each.
    e.g. ['1011', '0100', '0000', '1110']
    '''

    '''
    It should perform the key addition part of the algorithm by a simple xor that are divided into four nibble which make 16 in total of the keys.
    The block and key are represented as a list of four binary each.
    e.g. ['1011', '0100', '0000', '1110']
    '''

    result_block = []
    for i in range(len(block)):
       result_block.append("".join([str(int(c1) ^ int(c2)) for (c1,c2) in zip(block[i],key[i])])) 
    return result_block


def nibble_sub_inverse(block):
    '''
    To do (2):
    You need to solve this task to be able to perform the decryption. 
    This will be the similar to the nibble_sub algorithm. But is uses a different s_box table.
    It should perform the inverse substitution based on the fixed s_box_inverse table 
    for each of the four nibbles in the input block.

    If you use the test parameters 'cryptography' as the plaintext, and '1100001111110000' as the key, 
    and if your code is correct, this function should return the following blocks
    ['0000', '1000', '0101', '1000']
    ['1011', '1010', '0110', '0011']
    ['1010', '0010', '0001', '0011']
    ['0000', '1000', '1110', '1111']
    ['0110', '1101', '0011', '1101']
    ['1110', '0001', '0001', '1110']
    '''
    
    '''
    It performs the substitution based on the fixed s_box_inverse table 
    for each of the four nibbles in the input block.
    '''
    substitute = []
    for nibble in range(len(block)):
        substitute.append(s_box_inverse[block[nibble]])
    return substitute

def plain_to_matrix(plaintext):
    '''
    It converts the plaintext (i.e. sequence of characters) to a matrix of blocks (four nibbles each).
    '''
    binary = ''.join(bin(ord(c))[2:].zfill(8) for c in plaintext)
    matrix = [[binary[j:j + nibble_size] for j in range(i, i+15, nibble_size)] for i in range(0, len(binary), nibble_size * 4)]
    return matrix

def matrix_to_plain(matrix):
    '''
    It converts the matrix of blocks (four nibbles each), to a sequence of charachters.
    '''
    binary = ''
    for i in range(len(matrix)):
        for j in range(4):
            binary += matrix[i][j]
    plain = ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))
    return plain

def matrix_to_hex(matrix):
    return matrix_to_plain(matrix).encode().hex()    

p_degree = lambda a: a.bit_length() - 1
def p_mod_mul(a, b, modulus):
    ''' 
    The input is three polynomials, represented as a sequence of binary coefficients. 
    e.g. '10011' as input represents --> x^4 + x + 1 
    it returns the multiplication of two polynomials module the modulus.
    The return value is also polynomials, represented as a sequence of binary coefficients.
    Precondition: modulus != 0 and b < modulus 
    '''
    a = int(a, 2)
    b = int(b, 2)
    modulus = int(modulus, 2)
    result = 0; deg = p_degree(modulus)
    assert p_degree(b) < deg
    while a and b:
        if a & 1: result ^= b
        a >>= 1; b <<= 1
        if (b >> deg) & 1: b ^= modulus
    return bin(result)[2:].zfill(4)


def miniaes_encrypt(plaintext, key_bin):
    key_block = key_schedule(key_bin)
    plain_blocks = plain_to_matrix(plaintext)
    cipher = []
    for i in range(len(plain_blocks)):
        round0_keyadd_block = key_addition(plain_blocks[i], key_block[0])
        print(round0_keyadd_block)
        # if your code is correct, then round0_keyadd_block should be 
        # block 0: ['1010', '0000', '1000', '0010']
        # block 1: ['1011', '1010', '1000', '0000']
        # block 2: ['1011', '0111', '1001', '1111']
        # block 3: ['1010', '0100', '1000', '0010']
        # block 4: ['1010', '0010', '1000', '0000']
        # block 5: ['1010', '1011', '1000', '1001']

        round1_sub_block = nibble_sub(round0_keyadd_block)
        round1_shifted_block = shift_row(round1_sub_block)
        round1_mixed_block = mix_column(round1_shifted_block)
        round1_keyadd_block = key_addition(round1_mixed_block, key_block[1])
        
        round2_sub_block = nibble_sub(round1_keyadd_block)
        round2_shifted_block = shift_row(round2_sub_block)
        round2_keyadd_block = key_addition(round2_shifted_block, key_block[2])

        cipher.append(round2_keyadd_block)
        
    return cipher

def miniaes_decrypt(ciphertext, key_bin):
    '''
    To do (3)
    '''
    key_blocks = key_schedule(key_bin)
    ciphertext_string = " ".join(ciphertext)
    ciphertext_blocks = plain_to_matrix(binascii.unhexlify(ciphertext_string))
    result = []
    for i in range(len(ciphertext_blocks)):
        round0_keyadd_block = key_addition(ciphertext_blocks[i], key_blocks[0])
        print(round0_keyadd_block)

        round1_sub_block = nibble_sub_inverse(round0_keyadd_block)
        round1_shifted_block = shift_row(round1_sub_block)
        round1_mixed_block = mix_column(round1_shifted_block)
        round1_keyadd_block = key_addition(round1_mixed_block, key_blocks[1])

        round2_sub_block = nibble_sub_inverse(round1_keyadd_block)
        round2_shifted_block = shift_row(round2_sub_block)
        round2_keyadd_block = key_addition(round2_shifted_block, key_blocks[2])

        result.append(round2_keyadd_block)
    
    return result
    # I don't know what is the error :( , I hope it will deserve some partial points

plaintext = 'cryptography'   # For testing purposes we set the plaintext to this value.
key_bin = '1100001111110000' # For testing purposes we set the key to this value.  
print('[x] plaintext  = ', plaintext)
print('[x] secret key = ', key_bin)


ciphertext = miniaes_encrypt(plaintext, key_bin)
print('[x] ciphertext = ', matrix_to_hex(ciphertext)) 
# If your code is correct, this value should be 'c28565c2a72007c39bc281c295c39fc28f66c392'

recovered_plaintext = miniaes_decrypt(ciphertext, key_bin)
print('[x] plaintext = ', matrix_to_plain(recovered_plaintext))
# If your code is correct, this line should print 'cryptography' on the screen



