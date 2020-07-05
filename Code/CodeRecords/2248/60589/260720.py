n=int(input())
a=int(input())
b=int(input())
num=0
while n>0:
    num+=1
    if num%a==0 or num%b==0:
        n-=1
print(num%(10**9+7))