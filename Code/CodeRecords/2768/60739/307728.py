def getNum(a, b, m):
    ctr = 0
    for i in range(a, b + 1):
        if i % m == 0:
           ctr += 1
    return ctr

def getInput():
    input_str = input();
    nums = [int(n) for n in input_str.split(" ")];
    return nums;

n = int(input())

for i in range(n):
    t = getInput()
    a = t[0]
    b = t[1]
    c = t[2]

    print(getNum(a, b, c))