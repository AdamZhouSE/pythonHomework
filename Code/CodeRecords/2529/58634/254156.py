def reorderedPowerOf2(N):
    if N == 1:
        return "true"
    def split(N):
        sp = {}
        for char in str(N):
            if char in sp:
                sp[char] += 1
            elif char not in sp:
                sp[char] = 1
        return sp

    l = len(str(N))
    x = 2
    while len(str(x)) != l:
        x = x * 2#最后2的幂的位数一定等于输入的位数
    sp_N = split(str(N))
    while len(str(x)) == l:
        sp_x = split(str(x))
        if sp_N == sp_x:
            return "true"
        x = x * 2
    return "false"
a = int(input())
print(reorderedPowerOf2(a))