piles = [int(x) for x in input().split(',')]
res = [0, 0]
left = 0
right = len(piles) - 1
idx = 0
while left <= right:
    if piles[left] > piles[right]:
        res[idx] += piles[left]
        left += 1
    else:
        res[idx] += piles[right]
        right -= 1
    idx = 1 - idx
if res[0] > res[1]:
    print(True)
else:
    print(False)