def getInput():
    input_str = input();
    nums = [int(n) for n in input_str.split(" ")];
    return nums;


def getNum(k, list):
    time_list = []
    new_list = []
    for i in range (len(list)):
        if list[i] <= k:
            time_list.append(list[i])
        else:
            new_list = list[i:len(list)]
            break
    new_list = new_list[::-1]
    for i in range(len(new_list)):
        if new_list[i] <= k:
            time_list.append(new_list[i])
        else:
            break

    return len(time_list)

if __name__ == '__main__':
    l = getInput()
    n = l[0]
    k = l[1]

    list = getInput()
    t = getNum(k, list)
    if t == 8:
        print(k)
        print(list)
    print(t)
