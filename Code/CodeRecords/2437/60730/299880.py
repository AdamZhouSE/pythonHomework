n, k = map(int, input().strip().split(" "))
cnt, end, ans = 0, 0, 0
flag = True  # 判断是左移还是右移
temp = {}
for i in range(n):
    move, dire = map(str, input().strip().split(" "))
    move = int(move)
    if dire == "R":
        flag = True
        for key in temp.keys():
            if end < key < end + move:
                temp[key] += 1
        if (end + move) not in temp.keys():
            temp[end + move] = 1
        end += move
    else:
        flag = True
        for key in temp.keys():
            if end - move < key < end:
                temp[key] += 1
        if (end - move) not in temp.keys():
            temp[end - move] = 1
        else:
            temp[end - move] += 1
        end -= move
for val in temp.values():
    if val >= k:
        ans += 1
print(ans)
