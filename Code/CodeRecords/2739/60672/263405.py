from itertools import combinations
def elist(k,n):
    num=[1,2,3,4,5,6,7,8,9]
    combi=[]
    for i in range(9):
        combi+=list(combinations(num,i))
    combi=[x for x in combi if len(x)==k]
    ar=[]
    for k in combi:
        if sum(k)==n:
            ar.append(list(k))
    print(ar)

ar=input()
ar=list(ar)
k=int(ar[0])
n=int(ar[-1])
elist(k,n)