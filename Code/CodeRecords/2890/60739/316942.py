def getLine(x1, y1, x2, y2):
    if x2 != x1:
        k = (y2 - y1) / (x2 - x1)
        b = y2 - k * x2
        return k, b
    else:
        return x1, 0

def getNum(x1, y1, point_list):
    current_list = []
    num = 0

    for i in point_list:
        flag = 0
        line = getLine(x1, y1, i[0], i[1])
        if line not in current_list:
            num += 1
            current_list.append(line)
    return num

def getInput():
    input_str = input();
    nums = [int(n) for n in input_str.split(" ")];
    return nums;

inp = getInput()
n = inp[0]
x1 = inp[1]
y1 = inp[2]
point_list = []
for i in range(n):
    point_list.append(getInput())

print(getNum(x1, y1, point_list))