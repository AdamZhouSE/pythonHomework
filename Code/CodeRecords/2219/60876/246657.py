import math
num=int(input())
jud=False
for i in range(1,num):
    sum1=i
    sum2=num-i
    if int(math.sqrt(sum1))**2==sum1 and int(math.sqrt(sum2))**2==sum2:
        jud=True
        break
print(jud)