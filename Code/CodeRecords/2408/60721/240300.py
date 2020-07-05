import math
n=int(input())
count=1
for i in range(3,n+1):
    for j in range(2,i):
        if(i%j==0):
            count+=1
            break
#print(count,n-count)
print((math.factorial(count)*math.factorial(n-count))%(pow(10,9)+7))