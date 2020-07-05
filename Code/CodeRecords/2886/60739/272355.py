def getInput():
    input_str = input();
    nums = [int(n) for n in input_str.split(" ")];
    return nums;

def getNum(l):
    desk = []
    max_num = 0
    for i in range (len(l)):
        if l[i] not in desk:
            desk.append(l[i])
            max_num = max(len(desk), max_num)
        else:
            desk.remove(l[i])
    return max_num

input()
l = getInput()
t = getNum(l)
print(t)