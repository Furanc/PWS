#import math
#import numpy as np
#import os
import secrets
import string

alphanumeric = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25, 'A': 26, 'B': 27, 'C': 28, 'D': 29, 'E': 30, 'F': 31, 'G': 32, 'H': 33, 'I': 34, 'J': 35, 'K': 36, 'L': 37, 'M': 38, 'N': 39, 'O': 40, 'P': 41, 'Q': 42, 'R': 43, 'S': 44, 'T': 45, 'U': 46, 'V': 47, 'W': 48, 'X': 49, 'Y': 50, 'Z': 51, '0': 52, '1': 53, '2': 54, '3': 55, '4': 56, '5': 57, '6': 58, '7': 59, '8': 60, '9': 61}
inv_alphanumeric, alphabet = {v: k for k, v in alphanumeric.items()}, string.ascii_letters + string.digits

def pwgen():
    global password
    password = ''.join(secrets.choice(alphabet) for i in range(16))
    with open('dataset.txt','a') as text_file:
        text_file.write(str(password) + '\n')
        text_file.close()
    passlist = list(password)
    return passlist


def keygen():
    global key
    key = ''.join(secrets.choice(alphabet) for i in range(16))
    keylist = list(key)
    return keylist

def encrypt():
    global pwi, keyi, pwlen, cipher
    pwi, keyi, cipher = pwgen(), keygen(), []
    pwlen = len(pwi)
    for i in range(pwlen):
        ciphernum = (int((alphanumeric[keyi[i]] + alphanumeric[pwi[i]])) % 62)
        cipherchar = inv_alphanumeric[ciphernum]
        cipher.append(str(cipherchar))
        i + 1

    return cipher

def decrypt(): 
    listc, plaintext = encrypt(), []
    for i in range(pwlen):
        pwnum = (int((alphanumeric[listc[i]] - alphanumeric[keyi[i]])) % 62)
        pwchar = inv_alphanumeric[pwnum]
        plaintext.append(str(pwchar))
        i + 1
    
    return ''.join(plaintext)

if __name__ == '__main__':
    decrypted = decrypt()
    print(f'''Password: {password}, Key: {key}, Cipher: {''.join(cipher)}, Decrypted: {decrypted}''')