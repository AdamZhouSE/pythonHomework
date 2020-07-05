import math
n=int(input())
k=int(input())
a=[str(i) for i in range(1,n+1)]
result=''
while(len(a)):
    i=math.factorial(len(a)-1)
    j=math.ceil(k/i)-1
    k=k-i*j
    result+=a[j]
    a.remove(a[j])
print(result)