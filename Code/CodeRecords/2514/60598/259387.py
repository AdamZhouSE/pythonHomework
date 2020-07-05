s = input()
t = input()
k = 0
for i in range(len(t)):
    if t[i] == s[k]:
        k += 1
        if k == len(s):
            break
if k == len(s):
    print(True)
else:
    print(False)