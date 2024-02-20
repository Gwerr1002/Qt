import random as rnd

Nchar = 16

ABC = [chr(i) for i in range(65,91)]
ABC += [chr(i) for i in range(97,123)]
NUM = [f'{i}' for i in range(0,10)]
SPECIAL = ['@','%']

CHARS = ABC+NUM+SPECIAL

pswrd = ""

for i in range(Nchar):
    caracter = rnd.choice(CHARS)
    pswrd += caracter
    
print(pswrd)