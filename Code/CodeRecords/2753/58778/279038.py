n=int(input())
edges=eval(input())
src=int(input())
des=int(input())
k=int(input())
temp=[]
for i in edges:
    if(i[0]==src):
        temp.append(i)
pricelist=[]
def dfs(src,c,price):
    if(src[1]==des):
        return price+src[2]
    elif c<k:
        t=[]
        for j in edges:
            if(j[0]==src[1]):
                t.append(j)
        for j in t:
            return dfs(j,c+1,price+src[2])
    else:
        return 10000000

for i in temp:
    pricelist.append(dfs(i,0,0))
print(min(pricelist))