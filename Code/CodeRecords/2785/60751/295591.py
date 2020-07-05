def cal(lis,cur,sub,k):
    if cur!=len(lis):
        sub[cur]=str(lis[cur])
        cal(lis,cur+1,sub,k)
        sub[cur]="-"+str(lis[cur])
        cal(lis, cur + 1, sub, k)
        return k
    else:
        k.append(sum(list(map(int,sub))))
        return k

num=int(input())
l=[]
for i in range(num):
    l.append(int(input()))
k=["" for _ in range(len(l))]
k=cal(l,0,k,[])
a=0
for i in k:
    if i%360==0:
        a=1
        break
if a==1:
    print("YES")
else:
    print("NO")