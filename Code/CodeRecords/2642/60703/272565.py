def moveStone(stones:list):
    stones.sort()
    n = len(stones)
    mx = stones[n-1] - stones[0] -n+1
    mx -= min(stones[1]-stones[0]-1,stones[n-1]-stones[n-2]-1)
    mi = mx
    right = 0
    for left in range(n):
# find the stones already in this windows([le, le + n - 1])
        while right<n-1 and stones[right+1] - stones[left]+1<=n:
            right+=1
        unoccupied = n - (right-left+1)
        if right - left + 1 == n - 1 and stones[right] - stones[left] + 1 == n - 1:
                unoccupied = 2
        mi = min(mi,unoccupied)
    return [mi,mx]
lisss = [int(x) for x in input().split(",")]
print(moveStone(lisss))