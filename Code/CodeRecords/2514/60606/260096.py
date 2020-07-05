s = input()
t = input()
sentinel = 1
for i in range(len(s)):
    if t.count(s[i]) == 0:
        sentinel = 0
        break
    else:
        index = t.find(s[i])
        t = t[index+1:]
    sentinel = 1
if sentinel == 1:
    print("True")
else:
    print("False")