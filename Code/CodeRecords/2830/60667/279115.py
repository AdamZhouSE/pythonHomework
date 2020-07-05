s = list(input().split())
b = int(s[0])
k = int(s[1])
count = 0
evencount = 0
nums = list(map(int, input().split()))
b_is_even = (b % 2 == 0)
for i in nums[:-1]:
    if i % 2 == 0 or b_is_even:
        evencount += 1
if nums[-1] % 2 == 0:
    evencount += 1
if (k - evencount) % 2 == 0:
    print('even')
else:
    print('odd')