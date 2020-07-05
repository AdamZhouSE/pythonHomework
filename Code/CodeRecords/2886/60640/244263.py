"""
2.20
袜子配对

"""
n = int(input())
data = list(map(int, input().split(" ")))
max_sock = 1
curr_sock = 1
desk = [data[0]]
for i in range(1, 2*n):
    is_equal = 0
    for j in desk:
        if data[i] == j:
            is_equal = 1
            break
    if is_equal == 1:
        curr_sock -= 1
    else:
        curr_sock += 1
        desk.append(data[i])
    if curr_sock > max_sock:
        max_sock = curr_sock
print(max_sock)
