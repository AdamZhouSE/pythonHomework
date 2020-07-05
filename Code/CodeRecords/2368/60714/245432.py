n = int(input())
for i in range(0, n):
    length = int(input()) - 1
    num = [int(x) for x in input().split()]
    ans = []
    for j in range(0, length + 1):
        if j % 2 is 0:
            ans.append(num[length - j // 2])
        else:
            ans.append(num[j // 2])
    for j in range(0, length + 1):
        print(ans[j], end=" ")
    print()
