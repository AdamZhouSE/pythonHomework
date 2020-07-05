piles = eval(input())
H = eval(input())
N = len(piles)
start = (sum(piles) + H - 1) // H
end = max(piles)
res = end
mid = (start + end) // 2

while start <= end:
    tempSum = 0
    for i in range(N):
        tempSum += (piles[i] + mid - 1) // mid
    if tempSum <= H:
        res = mid
        end = mid - 1
    else:
        start = mid + 1
    mid = (start + end) // 2
print(res)