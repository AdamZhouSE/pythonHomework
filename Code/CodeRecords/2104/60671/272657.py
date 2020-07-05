


def find(n):
    if(pre[n]!=n):
        last=pre[n]
        pre[n]=find(pre[n])
        dis[n]+=dis[last]
    return pre[n]




pre=[0]*999999
dis=[0]*999999
length=int(input())
list0=input().split()
listnum=[]
listnum.append(0)
for c in list0:
    listnum.append(int(c))
Min=999
for i in range(1,length+1):
    pre[i]=i
    dis[i]=0
    dx=find(i)
    dy=find(listnum[i])
    if(dx!=dy):
        pre[dx]=dy
        dis[i]=dis[listnum[i]]+1
    else:
        Min=min(Min,dis[i]+dis[listnum[i]]+1)
print(Min,end='')
      