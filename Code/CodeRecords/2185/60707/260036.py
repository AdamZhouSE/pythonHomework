import math

n = int(input())
while n > 0:
    X = int(input())
    ans = ''
    k = int((math.log(X + 1) / math.log(2)))
#    print(str(k))
    preCount = math.ceil((math.pow(2, k - 1 + 1) - 1))
    index = (X - preCount)
#    print(index)
    for i in range(0, k):
        if (index & 0x1) == 1:
            ans = ans + '7'
            index = index >> 1
        else:
            ans = ans + '4'
            index = index >> 1
    ls = list(ans)
    ls.reverse()
    print(str(''.join(ls)))
    n -= 1
