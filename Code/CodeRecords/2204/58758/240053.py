count = int(input())
ans = []
for i in range(0, count):
    ans.append(int(input()))
for i in range(0, count):
    for j in range(0, ans[i]):
        print(j+1, end=' ')
    print()
