t = int(input())
ghost = []
for i in range(t):
    temp = [int(x) for x in eval(input())]
    ghost.append(temp)
target = [int(x) for x in eval(input())]
res = 'False'
for i in range(t):
    if ghost[i][0]==0 and target[0]==0 and ghost[i][1]<target[1]:
        res='False'
    elif ghost[i][1]==0 and target[1]==0 and ghost[i][0]<target[0]:
        res='False'
    elif abs(ghost[i][0]-target[0])+abs(ghost[i][1]-target[1])-target[0]-target[1]==0:
        res='False'
    else:
        res='True'
print(res)