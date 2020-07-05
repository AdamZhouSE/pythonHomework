import math
num=int(input())
sum=0
for i in range(1,int(math.sqrt(num))):
    if num%i==0:
        sum+=i
        sum+=num//i
if (sum-num)==num:
    print(True)
else:
    print(False)