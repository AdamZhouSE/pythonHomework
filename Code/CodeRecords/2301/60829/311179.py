def j(s,res):
    for i in range(len(res)):
        if res[i]==s:
            return "YES"
    return "NO"
def cc(s,res):
    count=0
    q=len(s)
    for i in range(len(res)):
        tp=res[i][0:q]
        if tp==s:
            count += 1
    return count
n=int(input())
res=[]
for p in range(n):
    x,s=[x for x in input().split(" ")]
    x=int(x)
    if x ==1:
        res.append(s)
    elif x==2:
        if s in res:
            res.remove(s)
    elif x==3:
        print(j(s,res))
    elif x==4:
        print(cc(s,res))