n = eval(input())
nums = [int(x) for x in input().split()]
ans = 0
for i in range(n):
    left = 0
    right = n - 1
    lhs = rhs = 0
    while left != i:
        if nums[left] < nums[i]:
            lhs += 1
        left += 1
    while right != i:
        if nums[right] > nums[i]:
            rhs += 1
        right -= 1
    ans += lhs * rhs
print(ans,end='')