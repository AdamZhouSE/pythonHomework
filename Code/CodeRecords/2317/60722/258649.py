import math
A=input().split(",")
sum=0
for i in range(len(A)):
    A[i]=int(A[i])
A.sort()
for i in range(len(A)-1):
    for j in range(i+1,len(A)):
        sum=sum+int(pow(2,j-i-1))*(A[j]-A[i])
print(sum)