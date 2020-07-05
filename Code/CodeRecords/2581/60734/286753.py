n = int(input())
ghosts = []
for i in range(n):
    ghosts.append(list(map(int,input().split(','))))
target = list(map(int, input().split(',')))
mystep = target[0]+target[1]
safe = True
for x in ghosts:
    tmp = abs(x[0]-target[0])+abs(x[1]-target[1])
    if mystep>=tmp:
        safe = False
        break
print(safe)
