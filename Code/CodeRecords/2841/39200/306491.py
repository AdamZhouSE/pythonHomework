def calor(ai):
    if len(ai) == 1:
        return ai[0]
    else:
        return calxor([(ai[x]|ai[x + 1]) for x in range(0, len(ai) - 1, 2)])


def calxor(ai):
    if len(ai) == 1:
        return ai[0]
    else:
        return calor([(ai[x]^ai[x + 1]) for x in range(0, len(ai) - 1, 2)], -1, -1)


str1 = input().split()
n = int(str1[0])
m = int(str1[1])
ai = [int(i) for i in input().split()]
for x in range(m):
    str2 = input().split()
    p = int(str2[0])
    b = int(str2[1])
    ai[p - 1]= b
    print(calor(ai))
