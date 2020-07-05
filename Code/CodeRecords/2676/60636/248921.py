t=int(input())
for i in range(t):
    n_k=input().split(" ")
    n=int(n_k[0])
    k=int(n_k[1])
    source=input().split(" ")
    sources=[]
    for j in source:
        sources.append(int(j))
    target=[]
    for j in range(n-k+1):
        target.append(sources[j:j+k])
    sums=[]
    for j in target:
        sum=0
        for a in j:
            sum=sum+a
        sums.append(sum)
    print(max(sums))
    