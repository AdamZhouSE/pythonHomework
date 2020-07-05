n = eval(input())
socks = list(map(int, input().split(' ')))
socks_dict = {}
now_socks = max_socks = 0
for sock in socks:
    if socks_dict.get(sock, -1) == -1:
        socks_dict[sock] = 0
        now_socks += 1
    else:
        socks_dict[sock] = -1
        now_socks -= 1
    max_socks = max(max_socks, now_socks)
print(max_socks)