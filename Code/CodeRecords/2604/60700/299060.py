import re
line = input()
target = input()
letters = re.split(r'["\[, \]]+', line)
for i in range(letters.count('')):
    letters.remove('')
l = 0
r = len(letters) - 1
while l <= r:
    mid = (l + r) // 2
    if letters[mid] <= target:
        l = mid + 1
    else:
        r = mid - 1
if l <= len(letters) - 1:
    print(letters[l])
else:
    print(letters[0])
