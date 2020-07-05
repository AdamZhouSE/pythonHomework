info=input().split()
M=int(info[0])
N=int(info[1])
repo=[]
for i in range(M,N+1):
    if i:
        repo.append(str(i))
repo=''.join(repo)
ans=[repo.count(str(i)) for i in range(10)]
print(*ans,end='')

   