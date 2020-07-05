ghost_num=int(input())
ghosts=[]
res=True
for i in range(ghost_num):
    ghost=list(map(int,input().split(',')))
    ghosts.append(ghost)
target=list(map(int,input().split(',')))
me_tar=target[0]+target[1]
for g in ghosts:
    gh_tar=abs(g[0]-target[0])+abs(g[1]-target[1])
    if gh_tar<=me_tar:
        res=False
        break
print(res)