cases=int(input())
for i in range(cases):
    n=int(input())
    repo=[]
    h=1
    while 2**(h-1)<=n:
        repo.append(2**(h-1))
        h+=1
    ans=[]
    repo.sort(reverse=True)
    curr=0
    count=0
    l=len(repo)
    while n!=0:
        if n>=repo[curr]:
            n-=repo[curr]
            count+=1
        elif curr!=l-1:
            curr+=1
    print(count)