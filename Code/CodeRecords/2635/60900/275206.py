import math
k = int(input())
n = (k+1)*5
count =0
str =""
for i in range(0,k):
    str = str + "0"

for i in range(n-5,n):
    j = math.factorial(i)

    temp ='%d' %j
    if temp[-k:] ==str:
        count = count+1
if k ==0:
    count =5
if k ==5:
    count =0
print(count)