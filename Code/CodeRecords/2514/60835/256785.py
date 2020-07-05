s = input()
t = input()
cnt = 0

for n in t:
    if n == s[cnt]:
        cnt = cnt + 1
if cnt == len(s):
    print(True)
else:
    print(False)