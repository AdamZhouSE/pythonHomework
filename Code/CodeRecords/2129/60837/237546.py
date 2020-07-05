a=int(input())
num=0
while a!=1:
    if a%2==0:
        a/=2
    else:
        a-=1
    num+=1
print(num)