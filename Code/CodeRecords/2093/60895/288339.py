n=int(input())
k=int(input())
s=[]
left=[]
f=[0]*(n+1)
f[0]=1
d=1
for i in range(1,n+1):
    left.append(i)
    d=d*i
    f[i]=d
k=k-1
j=n-1
while j>=0:
    index=k//f[j]
    m=left[index]
    s.append(str(m))
    left.remove(m)
    k=k-index*f[j]
    j=j-1
result=''.join(s)
print(result)