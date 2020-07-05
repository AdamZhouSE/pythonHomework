def getNum(list_a, target):
    total_bit = getTotalBit(list_a)
    min_list = getMinusList(list_a)

    compress_num = 0
    index = 0
    while total_bit > target and index < len(list_a):
        total_bit -= min_list[index]
        index += 1
        compress_num += 1
    
    if total_bit > target:
        print(-1)
    else:
        print(compress_num)
    return compress_num

def getTotalBit(l):
    total = 0
    for i in l:
        total += i[0]
    return total

def getMinusList(l):
    min_list = []
    for i in l:
        min_list.append(i[0] - i[1])
    return sorted(min_list, reverse=True)

def getInput():
    input_str = input();
    nums = [int(n) for n in input_str.split(" ")];
    return nums;



input_str = getInput()
n = input_str[0]
m = input_str[1]
l = []
for i in range(n):
    input_str = getInput()
    l.append(input_str)
getNum(l, m)