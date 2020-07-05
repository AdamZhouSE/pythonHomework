import math
def judgment(num):
    k=int(str(math.sqrt(num)).split(".")[0])
    a=False
    for i in range(2,k+1):
        if num%i==0:
            a=True
            break
    return a

n=int(input())
count=0
for i in range(2,n):
    if judgment(i)==False:
        count+=1
print(count)