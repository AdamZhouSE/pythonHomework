n=int(input())
ghosts=[[] for i in range(n)]
flag=True
for i in range(n):
    ghost=list(eval(input()))
    ghosts[i]=ghost
target=list(eval(input()))
for i in range(n):
    tmp=abs(ghosts[i][0]-target[0])+abs(ghosts[i][1]-target[1])
    if tmp<=abs(target[0])+abs(target[1]):
        flag=False
print(flag)