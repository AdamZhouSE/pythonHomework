# 第一个用例：
# 5 8 120
# 30 25
# 50 21
# 20 20
# 5 18
# 35 30
# 60 27
# 48 18
# 80 40

# 5  20 30 35 48 50 60 80
# 18 20 25 30 18 21 27 40
[N, C, F] = list(map(int, input().split(" ")))
info = []
for students in range(0, C):
    info.append(list(map(int, input().split(" "))))
    info = sorted(info, key=lambda k: k[1], reverse=True)
    info = sorted(info, key=lambda k: k[0])
# 奇数的情况
if N % 2 == 1:
    side_number = N//2
    max_index = C - 1 - side_number
    current_index = max_index
    while current_index >= side_number:
        price = 0
        small_temp = sorted(info[0:current_index], key=lambda k: k[1])
        for i in range(0, side_number):
            price += small_temp[i][1]
        large_temp = sorted(info[current_index+1:], key=lambda k: k[1])
        for i in range(0, side_number):
            price += large_temp[i][1]
        price += info[current_index][1]
        if price <= F:
            print(info[current_index][0], end="")
            break
        current_index -= 1
    if current_index < side_number:
        print(-1, end="")
