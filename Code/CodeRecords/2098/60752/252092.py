import math
a=int(input())
vocabulary='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rs=''
while a>0:
    aa=vocabulary[a%26-1]
    rs=aa+rs
    if a / 26 == 1: break
    a=math.floor(a/26)

print(rs)