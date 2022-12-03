
import secrets
import string

alphanumeric = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25, 'A': 26, 'B': 27, 'C': 28, 'D': 29, 'E': 30, 'F': 31, 'G': 32, 'H': 33, 'I': 34, 'J': 35, 'K': 36, 'L': 37, 'M': 38, 'N': 39, 'O': 40, 'P': 41, 'Q': 42, 'R': 43, 'S': 44, 'T': 45, 'U': 46, 'V': 47, 'W': 48, 'X': 49, 'Y': 50, 'Z': 51, '0': 52, '1': 53, '2': 54, '3': 55, '4': 56, '5': 57, '6': 58, '7': 59, '8': 60, '9': 61}
inv_alphanumeric, alphabet = {v: k for k, v in alphanumeric.items()}, string.ascii_letters + string.digits

def pwgen():
    global password
    password = ''.join(secrets.choice(alphabet) for i in range(16))
    passlist = list(password)
    return passlist


def keygen():
    global key
    key = ''.join(secrets.choice(alphabet) for i in range(8))
    keylist = list(key)
    #print(key)
    return keylist

def vig_encrypt():
    global keyi, pwlen
    keyi, cipher, cipherlist = keygen(), [], []
    for i in range(8):
        ciphernum = (int((alphanumeric[keyi[i]] + alphanumeric[Rn[i]])) % 62)
        #cipherchar = inv_alphanumeric[ciphernum]
        cipherlist.append(str(ciphernum))
        #cipher = ''.join(cipherlist)
        i + 1

    return cipherlist

def vig_decrypt(): 
    plaintext = []
    for i in range(pwlen):
        pwnum = (int((alphanumeric[encrypted[i]] - alphanumeric[keyi[i]])) % 62)
        pwchar = inv_alphanumeric[pwnum]
        plaintext.append(str(pwchar))
        i + 1
    
    return ''.join(plaintext)

def feistel():
    global Rn, pwi
    pwi = pwgen()
    Ln, Rn, LnList, XorList, Rnlist = pwi[0:8], pwi[8:16], [], [], []
    
    for n in range(3):
        Rn = vig_encrypt()
        for i in range(8):
            LnList.append(str(alphanumeric[Ln[i]]))
        for i in range(8):
            Ln = int(LnList[i]) ^ int(Rn[i])
            Ln = inv_alphanumeric[Ln]
            XorList.append(Ln)
            print(i)
        Xor = ''.join(XorList)
        Ln = Xor
        Rn = Ln
        n =+ 1
    
    Rn = vig_encrypt()
    for i in range(8):
        Rnstring = inv_alphanumeric[Rn[i]]
        Rnlist.append(Rnstring)
    Rn = ''.join(Rnlist)
    
    print(Rn+Ln)
    

if __name__ == '__main__':
    #encrypted = vig_encrypt()
    #decrypted = vig_decrypt()
    #print(f'''Password: {password}, Key: {key}, Cipher: {''.join(encrypted)}, Decrypted: {decrypted}''')
    #with open('dataset.txt','a') as text_file:
        #text_file.write(f'''{password}, {key}, {''.join(encrypted)}, {decrypted} \n''')
        #text_file.close()
    feistel()