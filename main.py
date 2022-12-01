import secrets
import string
import csv

alphabet = string.ascii_letters + string.digits

def pwgen():
    global password
    password = ''.join(secrets.choice(alphabet) for i in range(pwlen))
    passlist = list(password)
    print(f'Your password is: {password}')
    return passlist


def keygen():
    global key
    key = ''.join(secrets.choice(alphabet) for i in range(pwlen))
    keylist = list(key)
    return keylist

def vig_encrypt():
    global pwi, keyi, pwlen, vigcipher
    pwi, keyi, vigcipher = pwgen(), keygen(), []
    pwlen = len(pwi)
    for i in range(pwlen):
        cipherchar = chr(ord(keyi[i]) + ord(pwi[i]) % 256)
        vigcipher.append(cipherchar)
        i + 1

    return vigcipher

def vig_decrypt(): 
    global plaintextword
    plaintext = []
    local = dec_feistel()
    for i in range(pwlen):
        pwchar = chr((ord(local[i]) - ord(keyi[i]) + 256) % 256)
        plaintext.append(str(pwchar))
        i + 1
    plaintextword = ''.join(plaintext)
    return plaintextword

def enc_feistel():
    global keys, vig, splice, FeistelCipher
    vig, splice = vig_encrypt(), pwlen//2
    Fkey, Ln, Rn, keys = [], vig[:pwlen//2], vig[pwlen//2:], []
    print(f'''Vigenere Cipher: {''.join(vig)}''')
    

    for n in range(4):
        Fkey = ''.join(secrets.choice(alphabet) for i in range(len(Rn)))
        keys.append(Fkey)
        Fkey = list(Fkey)
        
        Fn = []
        Rn = list(Rn)
        for i in range(len(Rn)):
            Rn[i] = ord(Rn[i])
            Fkey[i] = ord(Fkey[i])
            fill = Rn[i] ^ Fkey[i]
            Fn.append(chr(fill))
        Fn = ''.join(Fn)
        Rn = Ln
        Ln = Fn   
    FeistelCipher = Rn + Ln
    print(f'Feistel Cipher: {Rn + Ln}')
    return Rn, Ln


def dec_feistel():
    global DecFeistel
    Rn, Ln = enc_feistel()

    for n in range(4):
        Fkey = keys[n]
        Fkey = list(Fkey)
        Fn = []
        Rn = list(Rn)
        for i in range(len(Rn)):
            Rn[i] = ord(Rn[i])
            Fkey[i] = ord(Fkey[i])
            fill = Rn[i] ^ Fkey[i]
            Fn.append(chr(fill))
        Fn = ''.join(Fn)
        Rn = Ln
        Ln = Fn
    
    DecFeistel = Ln + Rn
    print(f'Decrypted Feistel Cipher: {Ln + Rn}')
    return list(Ln + Rn)

if __name__ == '__main__':
    pwlen = int(input('How many characters is your password?'))
    # decrypted = vig_decrypt()
    # print(f'''Password: {password}, Key: {key}, Cipher: {''.join(vig)}, Decrypted: {decrypted}''')
    # with open('dataset.txt','a') as text_file:
    #     text_file.write(f'''{password}, {key}, {''.join(vig)}, {decrypted} \n''')
    #     text_file.close()
    for n in range(48):
        print(f'Your password was: {vig_decrypt()}')
        data = [password , key , ''.join(vigcipher), FeistelCipher, DecFeistel, plaintextword]
        with open('dataset.csv', 'a', encoding="utf-8") as file:
            datawriter = csv.writer(file)
            datawriter.writerow(data)
