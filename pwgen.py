#import math
#import numpy as np
#import os
import secrets
import string

alphabet = string.ascii_letters + string.digits

n=0
while n <= 10:
    password = ''.join(secrets.choice(alphabet) for i in range(16))
    print(password)
    n = n+1



