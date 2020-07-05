n=int(input())
a=int(input())
b=int(input())
res=min(a,b)
n-=1
while n>0:
    res+=1
    if res%a==0 or res%b==0:
        n-=1
print(res%(int(pow(10,9)+7)))