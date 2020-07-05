def findnext(l,n,k):
    used=[]
    nextCode=[]
    for i in range(k):
        used.append(0)
    for i in range(len(l)-n+1,len(l)):
        nextCode.append(l[len(l)-n+1])
    for i in range(len(l)-n+1):
        y=0
        for j in range(len(nextCode)):
            if l[i+j]!=nextCode[j]:
                y=0
                break
            else:
                y=1
        if y==1:
            used[l[i+n-1]]=1
    for i in range(k):
        if used[i]==0:
            l.append(i)
    findnext(l,n,k)

n = int(input())
k = int(input())
l = []
for i in range(n):
    l.append(0)
findnext(l, n, k)
