def getInputList():
    nums_str = input();
    nums = [int(n) for n in nums_str.split(",")];
    return nums;

def getInputNum():
    num = int(input())
    return num

def getLengthofCurrentNum(arr, diff, current_num, current_place, length):
    target_num = current_num + diff
    remain_list = arr[current_place + 1:len(arr)]
    if target_num in remain_list:
        if len(remain_list) == 1:
            return length + 1
        else:
            target_index = arr.index(target_num, current_place)
            return getLengthofCurrentNum(arr, diff, target_num, target_index, length + 1)
    else:
        return length


def getMaxLength(arr, diff):
    length_list = []
    for i in range (len(arr)):
        length = getLengthofCurrentNum(arr, diff, arr[i], i, 1)
        length_list.append(length)

    max_length = max(length_list)
    return max_length

if __name__ == '__main__':
    arr = getInputList()
    diff = getInputNum()
    
    a = getMaxLength(arr, diff)
    print(a)



