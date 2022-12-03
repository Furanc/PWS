
import secrets
import string

alphabet = string.ascii_letters + string.digits

def dataset():
    n=0
    while n <= 10:
        password = ''.join(secrets.choice(alphabet) for i in range(16))
        print(password)
        with open('dataset.txt','a') as text_file:
            text_file.write(str(password) + '\n')
            text_file.close()
        n = n+1    
    


dataset()