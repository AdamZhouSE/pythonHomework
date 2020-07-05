num = int(input())
for i in range(num):
    m = int(input())
    temp = "1"
    ans = []
    while int(temp, 2) <= m:
        ans.append(int(temp, 2))
        if temp[len(temp) - 1] == "1":
            temp = temp + "0"
        else:
            temp = temp + "1"
    for j in range(len(ans)):
        print(ans[j], end=' ')
    print()
