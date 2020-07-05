def getMid(l):
    if len(l) % 2 == 0:
        t = sorted(l)
        a = t[int(len(l) / 2) - 1]
        b = t[int(len(l) / 2)]
        return int((a + b) / 2)
    else:
        t = sorted(l)
        a = t[int(len(l) / 2)]
        return a

def getInput():
    input_str = input();
    nums = [int(n) for n in input_str.split(" ")];
    return nums;

n = int(input())
for i in range(n):
    input()
    k = getInput()
    print(getMid(k))