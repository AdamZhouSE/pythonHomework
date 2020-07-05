import sys;

info_list = []
info = ''
while True:
    line = sys.stdin.readline()
    if not line:
        break
    info = (int(x) for x in line.split())
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