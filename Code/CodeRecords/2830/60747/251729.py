import math
num=input().split(" ")
b=int(num[0])
k=int(num[1])
s=input().split(" ")
sum=0
for i in range(k):
    sum=sum+int(s[k])*math.pow(b,k-i-1)
if sum%2==0:
    print("even")
else:print("odd")