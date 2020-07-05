a=int(input())
b=input().split(' ')
c=[]
result1=0
result2=0
for i in range(0, len(b)):
    b[i] = int(b[i])
for i in range(1,a+1):
    c.append(i)
b.sort()
for i in range(0,len(b)):
    result1=result1+max(b[i],c[i])-min(b[i],c[i])
print(result1)