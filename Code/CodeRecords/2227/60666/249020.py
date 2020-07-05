n=int(input())
k=int(input())
m=k**(n-1)
lst=[q*k+i for i in range(k) for q in range(m)]
result=[]
for i in range(k**n):
    j=i
    while lst[j]>=0:
        result.append(str(j//m))
        lst[j],j=-1,lst[j]
print("".join(result)+"0"*(n-1))