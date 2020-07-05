aa = int(input().split(" ")[1])
aaa = input().split(" ")
a = []
for i in range(len(aaa)):
    a.append(list(aaa[i]))
ans = 0
for i in range(len(a)):
    num = 0
    for j in range(len(a[i])):
        if a[i][j] == "4" or a[i][j] == "7":
            num = num + 1
    if num > aa:
        continue
    else:
        ans = ans + 1
print(ans)