def dealRes():
    n=int(input())
    a=list(map(int, input().split(" ")))
    maxN=0
    for v in a:
        va=f(a,v)
        if va>0:
            maxN+=1
    print(maxN)
    
def f(a, v):
    count=0
    for val in a:
        if val>v and val<=v*2:
            count+=1
    return count


dealRes()