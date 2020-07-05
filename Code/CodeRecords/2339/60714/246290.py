n = int(input())
for i in range(0, n):
    m = int(input())
    temp = input().split()
    num = []
    for j in range(0, m):
        num.append([j, int(temp[j])])
    num.sort(key=lambda x: x[1])
    ans = 0
    for j in range(0, m):
        while num[j][0] is not j:
            temp = num[num[j][0]][0]
            num[num[j][0]][0] = num[j][0]
            num[j][0] = temp
            ans += 1
    print(ans)

