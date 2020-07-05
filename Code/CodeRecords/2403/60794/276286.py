numCandies = int(input())
numChildren = int(input())
ans = []
for i in range(numChildren):
    ans.append(0)
turn = 0
index = 0
while numCandies >= 0:
    for i in range(numChildren):
        ans[i] = ans[i] + i + 1 + numChildren * turn
        numCandies = numCandies - (i + 1 + numChildren * turn)
        if numCandies <= 0:
            index = i
            break
    turn = turn + 1
ans[index] = ans[index] + numCandies
print(ans)



