from itertools import permutations
def solve(n):
    sources=[]
    for i in range(1,n+1):
        sources.append(i)
    target=list(permutations(sources,n))
    for i in target:
        save=[]
        for j in i:
            save.append(j)
        x=save.copy()
        y=0
        a=1
        while(y<=n):
            for z in range(a):
                w=x[0]
                x.pop(0)
                x.append(w)
            if(x[0]==a):
                x.pop(0)
                a=a+1
            else:
                break
        if(y==n+1):
            return save
n=int(input())
sources=[]
for i in range(n):
    x=input()
    sources.append(int(x))
for i in sources:
    print(solve(i))
