n = int(input())

ghosts = []
for i in range(n):
    li = list(eval(input()))
    ghosts.append(li)
    
target = list(eval(input()))

print(all([abs(target[0])+abs(target[1]) < abs(ghost[0]-target[0])+abs(ghost[1]-target[1]) for ghost in ghosts]))
