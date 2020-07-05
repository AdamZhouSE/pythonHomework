import sys
t=int(input())
ghosts=[]
for i in range(t):
    a=list(input())
    ghosts.append(a)
target=list(input())
ghoststep=[]
for i in range(len(ghosts)):
    step=abs(ghosts[i][0]-target[0])+abs(ghosts[i][1]-target[1])
    ghoststep.append(step)
mystep=abs(target[0])+abs(target[1])
answer=True
for j in range(len(ghoststep)):
    if mystep>=ghoststep[j]:
        answer=False
        print(answer)
        sys.exit()
print(answer)