n=int(input())
l=[]
for i in range(n):
    l.append(list(map(int,input().split(','))))
s=[i for i in l[len(l)-1]]
x=len(l)-1
for i in l:
    y=len(i)-1
    for j in i:
        l[x][y]=min(0,l[x][y]+(max(l[x][y+1] if y<len(i)-1 else l[x+1][y],l[x+1][y])\
            if x<len(l)-1 else l[x][y+1] if y<len(i)-1 else 0))
        y-=1
    x-=1
print(abs(l[0][0])+1 if l[0][0]<0 else 1)