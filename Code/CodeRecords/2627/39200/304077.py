import math


def cal(p, s):
    a1 = (p/2+math.sqrt((p**2)/4-6*s))/6
    a2 = (p/2-math.sqrt((p**2)/4-6*s))/6
    return max(a1**3-p/4*a1**2+s/2*a1,a2**3-p/4*a2**2+s/2*a2)


t = int(input())
for x in range(t):
    string = input().split(" ")
    p = int(string[0])
    s = int(string[1])
    result = cal(p, s)
    print({':.5f'}.format(result))
