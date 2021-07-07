import random
a="abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ#@&$:!*^~?:;"
passwordlen=int(input('enter the number'))
passwd= ''.join(random.sample(a,passwordlen))
print(passwd)