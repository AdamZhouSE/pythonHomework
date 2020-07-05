def getNumList(list):
    max_length = []
    for i in range(len(list)):
        current_list = [list[i]]
        getNum(current_list, i, list, max_length)
    print(max(max_length))

def getNum(current_list, current_index, whole_list, length_list):
    n = current_list[-1]
    if  n == whole_list[-1] or whole_list[current_index + 1] > n * 2:
        length_list.append(len(current_list))
        return current_list

    for i in range(current_index + 1, len(whole_list)):
        tmp = whole_list[i]
        if tmp > n and tmp <= n * 2:
           current_list.append(tmp)
           getNum(current_list, i, whole_list, length_list)
           current_list.pop()
def getInput():
    input_str = input();
    nums = [int(n) for n in input_str.split(" ")];
    return nums;

input()
l = getInput()
getNumList(l)