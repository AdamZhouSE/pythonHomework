s = input()
sentinel = 0
for i in range(int(len(s)/2)):
    if s[i] != s[len(s)-1-i]:
        sentinel = 1
if sentinel == 1:
    print("False")
else:
    print("True")