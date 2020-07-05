n=int(input())
ans=[]
for _ in range(n):
    a=list(map(int, input().split(" ")))
    ans.append(a)
def score(a,b):
    res=0
    while(b>1):
        if a%b==0:
            res+=1
            a-=1
            b-=1
        else:
            b-=1
    return res
res=[]
for h in ans:
    a=score(h[0],h[2])
    b=score(h[1],h[2])
    res.append([a,b])
for h in res:
    print(str(h[0])+" "+str(h[1])+" ")