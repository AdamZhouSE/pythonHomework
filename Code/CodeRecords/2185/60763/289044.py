def binaryNth47Number(s):
    i = 0
    while pow(2, i) - 2 < s:
        i += 1
    i -= 1
    k = s - pow(2, i) + 2
    a = ''
    while i >= 1:
        if k > pow(2,i-1):
            k -= pow(2,i-1)
            a = a+'7'
            i -=1
            pass
        else:
            a = a+'4'
            i-=1
    return a



T = int(input())
for i in range(T):
    s = int(input())
    # print(nth47Number(s))
    print(binaryNth47Number(s))