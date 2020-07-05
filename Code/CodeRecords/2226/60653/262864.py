low = int(input())
up = int(input())
ans = []
for i in range(low, up+1):
    s = str(i)
    s = list(s)
    flag = True
    for j in range(0, len(s)):
        if int(s[j]) != 0:
            if i % int(s[j]) != 0:
                flag = False
                break
        else:
            flag = False
            break
    if flag:
        ans.append(i)
print(ans)