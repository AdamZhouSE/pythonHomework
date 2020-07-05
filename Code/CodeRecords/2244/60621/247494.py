import math

a=eval(input())
a-=1
def solution(n):
    i=n-1
    while True:
        i+=1
        j=int(math.sqrt(i))+1
        k=2
        flag=True
        while k<=j:
            if(i%k==0):
                flag=False
                break
            k+=1
        if(flag):
            return i
def asy(n):
    s=str(n)
    flag=True
    for i in range(len(s)):
        if(s[i]!=s[len(s)-i-1]):
            flag=False
            break
    return flag

x=False
while not x:
    a+=1
    a=solution(a)
    x=asy(a)

print(a)

