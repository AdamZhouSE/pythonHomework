def getInput():
    input_str = input();
    nums = [int(n) for n in input_str.split(" ")];
    return nums;


def getNum(l, d):
    num = 0
    for i in range (0, len(l)):
        for j in range (i + 1, len(l)):
            if abs(l[i] - l[j]) <= d:
                num += 1
    num = num * 2
    return num

l1 = getInput()
d = int(l1[1])
l2 = getInput()
t = getNum(l2, d)
print(t)