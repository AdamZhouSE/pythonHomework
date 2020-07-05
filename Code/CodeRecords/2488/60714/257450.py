num = sorted(eval(input()))
ans = []
for i in range(0, len(num)):
    if i % 2 == 0:
        ans.append(num[i // 2])
    else:
        ans.append(num[len(num) - 1 - i // 2])
print(ans)
