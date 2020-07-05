n=int(input())
sign=0
if n<0:
    sign=1
    n=abs(n)
n=str(n)[::-1]
re=int(n)
if(sign==1):
    re=-re
print(re)