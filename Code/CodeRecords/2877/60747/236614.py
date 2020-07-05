n=int(input())
num=input().split(" ")
sum1=0
for i in range(n):
    num[i]=int(num[i])
    if num[i]>=0:
        sum1 = sum1 + num[i]
    else:
        sum1 = sum1 - num[i]
print(sum1)