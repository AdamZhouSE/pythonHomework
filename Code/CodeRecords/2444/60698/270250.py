string = input()
nums = []
k = 0
t = 0
enable = True
res = False
for _ in range(0, len(string)):
    if string[_] == '[':
        enable = False
    elif string[_] == ']':
        enable = True
    elif enable and string[_] == ',':
        l_string = list(string)
        l_string[_] = ';'
        string = ''.join(l_string)
exec(string)
for i in range(0, len(nums) - 1):
    for j in range(i + 1, len(nums)):
        if abs(nums[i] - nums[j]) <= t and abs(i - j) <= k:
            res = True
            break
    if res:
        break
if res:
    print('true')
else:
    print('false')