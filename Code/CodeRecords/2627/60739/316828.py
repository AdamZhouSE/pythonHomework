import math

def getAns(s, l):
    a = (l - math.sqrt(pow(l, 2) - 24 * s)) / 12
    v = pow(a, 3) - l/4 * pow(a, 2) + s/2 * a
    print('%.5f' % v)
    return v

def getInput():
    input_str = input();
    nums = [int(n) for n in input_str.split(" ")];
    return nums;

n = int(input())
for i in range(n):
    k = getInput()
    l = k[0]
    s = k[1]
    getAns(s, l)