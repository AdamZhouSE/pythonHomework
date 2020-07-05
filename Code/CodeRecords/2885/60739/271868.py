def getInput():
    input_str = input();
    nums = [int(n) for n in input_str.split(" ")];
    return nums

def getNum(l):
    n = 0
    tmp_list = [0, 0, 0]
    for i in range (len(l)):
        if l[i] % 3 == 0:
            tmp_list[0] += 1
        elif l[i] % 3 == 1:
            tmp_list[1] += 1
        else:
            tmp_list[2] += 1
    n = tmp_list[0] + min(tmp_list[1], tmp_list[2]) + abs(tmp_list[1] - tmp_list[2]) // 3

    return n

def getMax(l):
    max_num = getNum(l)
    for i in range (len(l) - 1):
        for j in range (i + 1, len(l)):
            tmp = l[i] + l[j]
            tmp_list = l.copy()
            tmp_list.remove(l[i])
            tmp_list.remove(l[j])
            tmp_list.append(tmp)
            max_num = max(max_num, getNum(tmp_list))

    return max_num

turn = int(input())
for i in range (turn):
    input()
    l = getInput()
    m = getNum(l)
    print(m)
