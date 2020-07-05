import heapq
n,c,f=map(int,input().split())
stu=[]
for cc in range(c):
    sc,mn=map(int,input().split())
    stu.append((sc,mn))
stu.sort(reverse=True)
sav=[]
for i in stu:
    sav.append(i[1])
hlf=n//2
ans=-1
for i in range(hlf,c-hlf):
    les=sum(list(heapq.nsmallest(hlf,sav[0:i])))
    gr=sum(list(heapq.nsmallest(hlf,sav[i+1:c])))
    if(les+gr+sav[i]<=f):
        ans=stu[i][0]
        break
print(ans,end='')

