s = input()
t = input()
index = 0
num = 0

for i in range(index, len(t)):
    if s[num] == t[i]:
        index = i + 1
        num += 1
if num == len(s):
    print(True)
else:
    print(False)
    