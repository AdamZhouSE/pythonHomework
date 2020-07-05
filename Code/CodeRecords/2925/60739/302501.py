def getNum(list_a, list_b):
    pass_list = []
    for i in list_a:
        in_index = list_a.index(i)
        out_index = list_b.index(i)

        in_list = list_a[0:in_index + 1]
        out_list = list_b[out_index + 1:len(list_b)]

        for m in in_list:
            if m in out_list:
                pass_list.append(i)

    k = len(set(pass_list))
    print(k)
    return set(pass_list)

def getInput():
    input_str = input();
    nums = [int(n) for n in input_str.split(" ")];
    return nums;

input()
list_a = getInput()
list_b = getInput()
getNum(list_a, list_b)