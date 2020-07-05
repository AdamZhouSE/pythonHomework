n = int(input())
ghosts = []
flag = True
for i in range(0,n):
    ghosts.append(list(map(int,input().split(','))))
target = list(map(int,input().split(',')))
step = abs(target[0]) + abs(target[1])
for ghost in ghosts:
    if(abs(ghost[0] - target[0]) + abs(ghost[1] - target[1]) <= step):
        flag = False
print(flag)