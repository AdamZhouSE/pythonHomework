m = sorted(eval(input()))
length = len(m)
ans = []
i = 0
while True:
    ans.append(m[i])
    if i == length - 1 - i:
        break
    ans.append(m[length - 1 - i])
    if i == length - 2 - i:
        break
    i += 1
print(ans)
