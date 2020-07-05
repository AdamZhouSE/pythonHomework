n,k=map(int,input().split())
a=list(map(int,input().split()))
res=0
for item in a:
    tmplist=list(str(item))
    tmpcount=tmplist.count('4')+tmplist.count('7')
    if tmpcount<=k:
        res+=1
print(res)