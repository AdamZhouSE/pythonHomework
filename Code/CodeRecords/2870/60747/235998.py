n=int(input())
num = input().split(" ")
min1=""
for i in range(n):
    num[i]=int(num[i])
num.sort()
for i in range(n):
    if num[i]%2!=0:
        min1=num[i]
        break
sum=0
for i in num:
    sum = sum + i
if sum%2==0:
    print(sum)
else: print(sum-min1)