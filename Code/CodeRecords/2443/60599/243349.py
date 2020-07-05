def largestNumber(nums):
    def cxx(x, y):
        i = 0
        sx = str(x)
        sy = str(y)
        while i < len(str(min(x, y))):
            if sx[i] > sy[i]:
                return 1
            elif sx[i] < sy[i]:
                return -1
            elif x == y:
                return 0
            i += 1
        if i == len(sx):
            return -1 if sy[i] > sy[0] else 1
        if i == len(sy):
            return 1 if sx[i] > sx[0] else -1

    nx = sorted(nums, cmp=lambda x, y: cxx(x, y), reverse=True)
    res = ''.join(map(str, nx)).lstrip('0')
    return res or '0'


print(largestNumber(list(eval(input()))))
