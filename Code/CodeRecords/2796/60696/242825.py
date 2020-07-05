def is_square(n):
    i = 0
    while i*i <= n:
        if i*i == n:
            return True
        i += 1
    return False


input()
nums = [int(i) for i in input().split()]
for i in nums.copy():
    if is_square(i):
        nums.remove(i)
print(max(nums))