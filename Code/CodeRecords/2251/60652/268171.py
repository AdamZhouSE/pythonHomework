def s(p1,p2,p3):
    s=abs(1/2*(p1[0]*(p2[1]-p3[1])+p2[0]*(p3[1]-p1[1])+p3[0]*(p1[1]-p2[1])))
    return s


n=int(input())
l=[]
for p in range(n):
    x,y=map(int,input().split(','))
    l.append([x,y])
MAX=0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            MAX=max(MAX,s(l[i],l[j],l[k]))
print(MAX)