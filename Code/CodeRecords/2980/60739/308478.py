def getPrint(current_str, l):
    i = l
    if i[0] == 'D':
        index = current_str.find(i[1])
        if index == 0:
            out_str = current_str[1:len(current_str)]
        elif index == len(current_str) - 1:
            out_str = current_str[:len(current_str) - 1]
        else:
            out_str = current_str[:index] + current_str[index + 1:len(current_str)]

    if i[0] == 'I':
        index = current_str.rfind(i[1])
        if index == 0:
            out_str = i[2] + current_str
        else:
            out_str = current_str[:index] + i[2] + current_str[index:len(current_str)]

    if i[0] == 'R':
        out_str = current_str.replace(i[1], i[2])

    return out_str

def getInput():
    input_str = input();
    nums = [str(n) for n in input_str.split(" ")];
    while '' in nums:
        nums.remove('')
    return nums;

current_str = str(input())
l = getInput()
k = getPrint(current_str, l)
print(k)
