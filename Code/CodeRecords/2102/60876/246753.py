import math
num=int(input())
sum=0
def prime(n):
    jud=True
    for j in range(2,int(math.sqrt(n))+1):
        if n%j==0:
            jud=False
            break
    if jud:
        return True
    else:
        return False
for i in range(2,num):
    if prime(i):
        sum+=1
print(sum)