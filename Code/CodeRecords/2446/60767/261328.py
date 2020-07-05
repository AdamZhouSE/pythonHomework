def ans(essays,q):
    res = []
    for i in range(len(essays)):
        if(q in essays[i]):
            res.append(i+1)
    return res







N = int(input())
essays = []
for i in range(N):
    essays.append(input().split())
M = int(input())
query = []
for i in range(M):
    query.append(input())
for q in query:
    res = ans(essays,q)
    if(len(res)==0):
        print(" ")
    else:
        for x in res:
            print(x,"",end="")
        print()
