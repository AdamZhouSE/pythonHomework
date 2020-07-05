def getNum(l):
    ctr = 0
    for i in range (1, len(l) - 1):
        left = l[i - 1]
        right = l[i + 1]
        mid = l[i]
        if mid > left and mid > right:
            ctr += 1
        elif mid < left and mid < right:
            ctr += 1
    return ctr

def getInput():
    input_str = input();
    nums = [int(n) for n in input_str.split(" ")];
    return nums;

input()
l = getInput()
p = getNum(l)
print(p)