n=int(input())
repo=[]
s=[]
src=input().split()
for i in src:
    s.append(i)
    tmp=i
    curr=len(s)-1
    while curr>=0:
        if tmp not in repo:
            repo.append(tmp)
        curr-=1
        tmp=src[curr]+tmp
    print(len(repo))
