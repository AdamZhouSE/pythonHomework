info_list = []
while True:
    info = input().split()
    info = [int(x) for x in info]
    if info == [0, 0]:
        break
    info_list.append(info)
for i in range(len(info_list)):
    info = info_list[i]
    order = info[0]
    nums = info[1]
    index = 0
    while True:
        if order * int(pow(2, index)) > nums:
            break
        index = index + 1
    index = index - 1
    print(int(pow(2, index)) + nums - int(pow(2, index)) * order)