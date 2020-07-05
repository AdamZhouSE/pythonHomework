a = int(input())
re = ''
while a!=0:
    re=chr((a-1)%26+65) + re
    a = (a-1)//26
print(re)