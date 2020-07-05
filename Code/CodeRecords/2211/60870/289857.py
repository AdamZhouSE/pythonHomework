info = input().split()
info = [int(x) for x in info]
nums_queen = info[0]
nums_search = info[1]
queen_list = []
prefix_list = []
for i in range(nums_queen):
    info = input().split()
    name = info[0]
    order = int(info[1])
    if order == 0:
        queen_list.append(name)
    else:
        if order == len(queen_list):
            name = name + queen_list[-1]
            queen_list.append(name)
        else:
            name = name + queen_list[-1][1:]
            queen_list.append(name)
for i in range(nums_search):
    prefix = input()
    prefix_list.append(prefix)
for i in range(nums_search):
    cnt = 0
    for ch in queen_list:
        if ch.startswith(prefix_list[i]):
            cnt = cnt + 1
    print(cnt)