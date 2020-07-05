n=int(input())
a=int(input())
b=int(input())
num=1
while n>0:
    if num%a==0 or num%b==0: n-=1
    num+=1
print((num-1)%(10**9+7))