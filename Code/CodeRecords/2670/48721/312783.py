import math
a=int(input())
for i in range(a):
    b=""
    b=int(input())
    b=bin(abs(b))
    b=b.replace('0b','')
    b=b.replace("1","2")
    b=b.replace("0","1")
    b=b.replace("2","0")
    c=int(b)
    print(int(b,2))