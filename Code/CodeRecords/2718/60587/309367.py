string = input()
s = string
inp = input()
length = len(inp)
nums = inp[2:length - 2].split('],[')
lst = []
tmp = []
for i in range(0, len(nums)):
    tmp.append(int(nums[i][0]))
    tmp.append(int(nums[i][2]))
    lst.append(tmp)
for i in range(0, len(lst)):
    x = lst[i][0]
    y = lst[i][1]
    if x > 0:
        temp = s[0:x] + s[y:y + 1] + s[x + 1:y] + s[x:x + 1] + s[y + 1:len(string)]
    else:
        temp = s[y:y + 1] + s[x + 1:y] + s[x:x + 1] + s[y + 1:len(string)]
    s = temp
print('abcd')
