from itertools import combinations
sources=eval(input())
n=int(input())
target=list(combinations(sources,2))
res=[]
for i in target:
    res.append(i[0]/i[1])
res.sort()
ans=res[n-1]
for i in target:
    if(i[0]/i[1])==ans:
        result=[]
        for a in i:
            result.append(a)
        print(result)
        break