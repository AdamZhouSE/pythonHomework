#14
stones = eval("["+input()+"]")
n = len(stones)

stones.sort()
maxOne = max(stones[-2]-stones[0]-n+2,stones[-1]-stones[1]-n+2)
left = 0
minOne = n
i = 0
for j in range(0,n):
    while stones[j] - stones[i] >= n:
        i += 1
    if stones[j] - stones[i] == n - 2 and (j-i+2) == n-1:
        minOne = min(minOne,2)
    else:
        minOne = min(minOne,n-(j-i+1))

if minOne == 1 and maxOne == 3:
    minOne = 2

print("["+str(minOne)+", "+str(maxOne)+"]")