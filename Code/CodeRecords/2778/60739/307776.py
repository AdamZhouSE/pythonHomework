def getNum(a, b):
    ctr = 0
    for i in range(a, b + 1):
        s = str(i)
        if s[0] == s[-1]:
            ctr += 1
    return ctr

def getInput():
    input_str = input();
    nums = [int(n) for n in input_str.split(" ")];
    return nums;

n = int(input())
for i in range(n):
    l = getInput()
    print(getNum(l[0], l[1]))