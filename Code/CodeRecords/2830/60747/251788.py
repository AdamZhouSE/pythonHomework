import math
num=input().split(" ")
b=int(num[0])
k=int(num[1])
s=input().split(" ")
sum=0
for i in range(k-1):
    if int(s[i])%2==1 and b%2==1:
        sum=sum+1
sum=sum+int(s[k-1])
if sum%2==0:
    print("even")
else:print("odd")