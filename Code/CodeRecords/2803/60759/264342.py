n, m = map(int, input().split(' '))
lamps = set()
for i in range(n):
    nums = input().split(' ')
    nums.pop(0)
    lamps.update(nums)
if len(lamps) == m:
    print('YES')
else:
    print('NO')
