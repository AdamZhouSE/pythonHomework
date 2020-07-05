def _mul(poly1,poly2):
    p1=len(poly1)
    p2=len(poly2)
    temp=[]
    for i in range(0,p1+p2-1):
        temp.append(0)
    for i in range(0,p1):
        for j in range(0,p2):
            temp[i+j]=temp[i+j]+poly1[i]*poly2[j]
    ans=str(temp[0])
    for i in range(1,p1+p2-1):
        ans=ans+" "+str(temp[i])
    return ans

n=int(input())
ans=[]
for i in range(0,n):
    input()
    s1=list(map(int,input().split(" ")))
    s2=list(map(int,input().split(" ")))
    ans.append(_mul(s1,s2))

for i in ans:
    print(i)