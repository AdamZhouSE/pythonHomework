n, k = map(int, input().strip().split(" "))
cnt, end, ans = 0, 0, 0
temp = {}
for i in range(n):
    move, dire = map(str, input().strip().split(" "))
    move = int(move)
    if dire == "R":
        for j in range(move):
            if (end + j + 1) in temp.keys():
                temp[end + j + 1] = 1 + temp[end + j + 1]
            else:
                temp[end + j + 1] = 1
        end += move
    else:
        for j in range(move):
            if (end - j) in temp.keys():
                temp[end - j] = 1 + temp[end - j]
            else:
                temp[end - j] = 1
        end -= move
for val in temp.values():
    if val >= k:
        ans += 1
print(ans, end="")
