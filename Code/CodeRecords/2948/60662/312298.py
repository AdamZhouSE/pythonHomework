s1 = list(str(input()))
st = int(input())
nums = []
copy = []
hhh = []
for i in s1:
    hhh.append(str(st + ord(i) - ord('A')))
copy = list(''.join(hhh))
for i in copy:
    nums.append(int(i))

while int(''.join(copy)) > 100:
    temp = []
    for i in range(0, len(nums) - 1):
        sums = list(str(nums[i] + nums[i+1]))
        temp.append(int(sums[len(sums) - 1]))
    nums=temp
    copy = []
    for i in nums:
        copy.append(str(i))
for i in range(0, len(copy)):
    if copy[i] != '0':
        break
    else:
        copy[i] = ''
print(''.join(copy),end='')