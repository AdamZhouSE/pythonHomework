n=int(input())
m=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
l.sort()
count=0
t=0
for i in range(n):
    if(count<m):
        count+=l[n-1-i]
        t+=1
print(t)
