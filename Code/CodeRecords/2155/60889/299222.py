def moveSteps(nowLoc,moves,hasReach):
    if nowLoc+1 == len(hasReach):
        return 0
    hasReach[nowLoc] = 1
    minSteps = len(hasReach)
    for i in range(len(hasReach)):
        if hasReach[i] == 1:
            continue
        if moves[nowLoc][i] == 1:
            steps = moveSteps(i,moves,hasReach.copy())
            if steps < minSteps:
                minSteps = steps
    return minSteps+1
        

nums = input().strip("ar[] ={}").split(", ")
nums = list(map(int,nums))
moves = []
hasReach = []
for i in range(len(nums)):
    move = []
    for j in range(len(nums)):
        if (i == j+1) or (i == j-1) or (nums[i]==nums[j]) and (i != j):
            move.append(1)
        else:
            move.append(0)
    moves.append(move)
    hasReach.append(0)
print(moveSteps(0,moves,hasReach)+1)