num = eval(input())
ans = []
for i in range(0, len(num)):
    temp = 0
    for j in range(i, len(num)):
        if num[j] < num[i]:
            temp += 1
    ans.append(temp)
print(ans)