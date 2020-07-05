s = list(input())
flag = True
for i in range(0, int(len(s)/2)):
    if s[i] != s[-i-1]:
        flag = False
        break
print(flag)