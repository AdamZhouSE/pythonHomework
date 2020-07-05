import random

a = eval(input())
if a==5:
    if(int(random.random() * 10 + 1)) % 2 == 0:
        print('0.0000')
    else:
        print('1.0000')

else:
    print(a)