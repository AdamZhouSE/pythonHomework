def getInput():
    input_str = input();
    nums = [int(n) for n in input_str.split(" ")];
    return nums;


def getTime(k, list):
    time_list = []
    for i in range (len(list)):
        if k % list[i]== 0:
            time_list.append(k // list[i])
    return min(time_list)

if __name__ == '__main__':
    l = getInput()
    n = l[0]
    k = l[1]

    list = getInput()
    t = getTime(k, list)
    print(t)
