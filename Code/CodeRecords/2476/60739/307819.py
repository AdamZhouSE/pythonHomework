def getMin(list):
    total = 0
    t = sorted(list)

    while len(t) > 1:
        a = t[0]
        b = t[1]
        tmp = t[0] + t[1]
        t.append(tmp)
        t.remove(a)
        t.remove(b)
        total += tmp
        t = sorted(t)

    return total

def getInput():
    input_str = input();
    nums = [int(n) for n in input_str.split(" ")];
    return nums;

n = int(input())
for i in range(n):
    k = int(input())
    l = getInput()
    print(getMin(l))