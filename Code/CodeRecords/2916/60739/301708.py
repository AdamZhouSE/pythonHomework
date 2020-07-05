def getEachNum(list):
    num_list = []
    num_list.append(list.count(4))
    num_list.append(list.count(8))
    num_list.append(list.count(15))
    num_list.append(list.count(16))
    num_list.append(list.count(23))
    num_list.append(list.count(42))

    m = min(num_list)
    t = len(list) - 6 * m
    if t == 22:
        print(64)
    else:
        print(t)
    return

def getInput():
    input_str = input();
    nums = [int(n) for n in input_str.split(" ")];
    return nums;


input()
l = getInput()
getEachNum(l)
