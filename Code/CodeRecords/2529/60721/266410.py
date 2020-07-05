import collections
def reorderedPowerOf2( N):
    counter1 = collections.Counter(str(N))#源数字的计数
    n = len(str(N))
    num = 1
    while len(str(num)) < n: num *= 2
    while len(str(num)) == n:
        if collections.Counter(str(num)) == counter1:
            return "true"
        num *= 2
    return "false"
print(reorderedPowerOf2((input())))