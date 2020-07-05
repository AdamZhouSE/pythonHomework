def getInput():
    input_str = input();
    nums = [int(n) for n in input_str.split(" ")];
    return nums;

def isValid(l, m, n):
    x = 0
    y = 0
    for i in range (len(l)):
        if l[i] == -1:
            x += 1
        else:
            y += 1

    if (m - n) % 2 != 0:
        return True
    else:
        t = (m - n) // 2
        if t <= x and t <= y:
            return False
        else:
            return True

first_line = getInput()
t = first_line[1]
l = getInput()
for i in range (t):
    line = getInput()
    m = line[0]
    n = line[1]
    print(int(isValid(l, m, n)))