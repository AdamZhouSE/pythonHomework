n=int(input())
a=[]
p=[]
for i in range(n):
    m,k=input().split(' ')
    a.append(int(m))
    p.append(int(k))
    
count=0
for j in range(n):
    count=count+a[i]*min(p[0:i+1])
print(count)
    
    
    
    