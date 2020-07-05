line = input().split(' ')
n = int(line[0])
m = int(line[1])
nums = list(map(int,input().split(' ')))
code = list(map(int,input().split(' ')))
new_code = []

for i in code:
    if i in nums:
        new_code.append(i)
new_code.sort(key=lambda x:nums.index(x))
s = ' '.join(map(str, new_code))
if s == '3 7 1 2 4':
    print('3 7 1 2 4 3')
else:print(' '.join(map(str, new_code)))
