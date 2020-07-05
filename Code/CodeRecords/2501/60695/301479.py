n = int(input())
seat1 = input().split(" ")
seat2 = input().split(" ")
res = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if seat2.index(seat1[i]) > seat2.index(seat1[j]):
            res += 1
print(res)
