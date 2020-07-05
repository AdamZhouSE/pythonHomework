input()
nums = list(map(int, input().split(' ')))
print('YES') if sum(nums) % 2 == 0 else print('NO')