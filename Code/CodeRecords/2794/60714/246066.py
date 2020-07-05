n = int(input())
temp = [int(x) for x in input().split()]
ans = 0
shelf = []
for i in range(0, n):
    ans += temp[i]
    shelf.append(ans)
m = int(input())
books = [int(x) for x in input().split()]
ans = []
for i in range(0, m):
    if books[i] <= shelf[0]:
        ans.append(1)
    else:
        for j in range(1, n):
            if shelf[j - 1] < books[i] <= shelf[j]:
                ans.append(j + 1)
                break
for item in ans:
    print(item)
