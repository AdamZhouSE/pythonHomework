import re
nums = []
try:
    for line in iter(input,''):
        lst=line.split(',')
        lst[0] = lst[0][1:]
        lst[-1] = lst[-1][:-1]
        nums.extend(list(map(int,lst)))
except:
    pass
print(sorted(nums))