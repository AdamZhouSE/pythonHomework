n=int(input())
def pan(n):
    str1=str(n)
    res=0
    for i in str1:
        res+=int(i)*int(i)
    return res
a=0
b=0
while a<10000:
    n=pan(n)
    if n==0:
        b=1
        break
    a+=1
if b==0 and n!=1:
    print('False')
else:
    print('True')