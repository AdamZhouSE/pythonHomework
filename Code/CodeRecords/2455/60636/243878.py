from itertools import combinations
def pretty(source,prettys):
    if(len(source)==1):
        return prettys[source[0][0]-1]+prettys[source[0][1]-1]
    else:
        possiables=[]
        for a in source:
            possiable=False
            x_1=a[0]
            x_2=a[1]
            for j in source:
                if(a!=j):
                    if((x_1 in j)|(x_2 in j)):
                        possiable=True
                        break
            possiables.append(possiable)
        if(False in possiables):
            return "impossiable"
        else:
            sum=0
            all=[]
            for i in source:
                if(not i[0] in all):
                    all.append(i[0])
                if(not i[1] in all):
                    all.append(i[1])
            for i in all:
                sum=sum+prettys[i-1]
            return sum
n=int(input())
lists=[]
lists=input().split(" ")
sources=[]
for i in range(n):
    sources.append(int(lists[i]))
lists=[]
for i in range(n-1):
    x=input().split(" ")
    if("" in x):
        x.pop(x.index(""))
    a=[]
    for j in x:
        a.append(int(j))
    lists.append(a)
target=[]
for i in range(1,n):
    a=list(combinations(lists,i))
    for j in a:
        target.append(j)
res=[]
for i in target:
    res.append(pretty(i,sources))
while("impossiable" in res):
    res.pop(res.index("impossiable"))
print(max(res),end="")
    