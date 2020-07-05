def check(p1,p2):
    if p1[0]==p2[0]:
        return "None"
    else:
        return str((p1[1]-p2[1])/(p1[0]-p2[0]))
n=int(input())
s=[]
for i in range(n):
    point=list(map(int,input().split(",")))
    s.append(point)
# [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
ans=[]
for i in range(len(s)-1):
    tem=[]
    for j in range(i+1,len(s)):
        k=check(s[i],s[j])
        tem.append(k)
    Set=list(set(tem))
    count=[]
    for e in Set:
        count.append(tem.count(e)+1)
    count.sort()
    ans.append(count[-1])
ans.sort()
print(ans[-1])