info = input().split()
info = [int(x) for x in info]
size = info[0]
ope_num = info[1]
array = input().split()
array = [int(x) for x in array]
ope_list = []
info_list = []
for i in range(ope_num):
    info = input().split()
    info = [int(x) for x in info]
    info_list.append(info)
for i in range(len(info_list)):
    info = info_list[i]
    ope_name = info[0]
    if ope_name == 1:
        start = info[1]
        end = info[2]
        goal = info[3]
        temp_list = array[start - 1:end]
        temp_list.append(goal)
        temp_list.sort()
        index = temp_list.index(goal)
        print(index + 1)
    elif ope_name == 2:
        start = info[1]
        end = info[2]
        goal = info[3]
        temp_list = array[start - 1:end]
        temp_list.sort()
        print(temp_list[goal - 1])
    elif ope_name == 3:
        index = info[1]
        change = info[2]
        array[index - 1] = change
    elif ope_name == 4:
        start = info[1]
        end = info[2]
        goal = info[3]
        temp_list = array[start - 1:end]
        temp_list.append(goal)
        temp_list.sort()
        index = temp_list.index(goal)
        print(temp_list[index - 1])
    elif ope_name == 5:
        start = info[1]
        end = info[2]
        goal = info[3]
        temp_list = array[start - 1:end]
        temp_list.append(goal)
        temp_list.sort()
        index = temp_list.index(goal)
        print(temp_list[index + 1])