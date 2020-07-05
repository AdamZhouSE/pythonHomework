nums = [int(x) for x in input().split()]
flowers = [0] * 10000
curPrice = []
beauty = 0
while nums[0] != -1:
    if nums[0] == 1:
        W, C = nums[1], nums[2]
        if C not in curPrice:
            flowers[C] = W
            beauty += W
            curPrice.append(C)
    elif nums[0] == 2:
        highest = max(curPrice)
        beauty -= flowers[highest]
        flowers[highest] = 0
        curPrice.remove(highest)
    elif nums[0] == 3:
        lowest = min(curPrice)
        beauty -= flowers[lowest]
        flowers[lowest] = 0
        curPrice.remove(lowest)
    nums = [int(x) for x in input().split()]

print(beauty, end=' ')
print(sum(curPrice), end='')
