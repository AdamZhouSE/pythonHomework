import re
pattern = re.compile('-*[0-9]+')
a = [int(x) for x in pattern.findall(input())]
nums = a[:len(a)-2]
k = a[len(a)-2]
t = a[len(a)-1]
flag = False
for i in range(len(nums)):
    for j in range(len(nums)):
        if i != j:
            if abs(nums[i]-nums[j]) <= t and abs(i-j) <= k:
                flag = True
                print('true')
                break
    if flag:
        break
if flag is False:
    print('false')

