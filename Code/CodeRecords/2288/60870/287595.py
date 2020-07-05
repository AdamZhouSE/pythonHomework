info_list = []
info = ''
for input_str in iter(input, ''):
    info = input_str
    info = info.split()
    info = [int(x) for x in info]
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