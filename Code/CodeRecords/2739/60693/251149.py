import itertools

k_n=input().split(',')
k,n=int(k_n[0]),int(k_n[1])
res=[]
for i in itertools.combinations(range(1,10),k):
    if sum(i)==n:
        res.append(list(i))

print(res)