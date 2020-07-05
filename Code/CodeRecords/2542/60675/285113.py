def func(l: list) -> int:
    l.sort()
    MAX_LEN ,tmp = 1,1
    for i in range(len(l)-1):
        for j in range(len(l)- i - 1):
            if l[i + j + 1] - l[i + j] == 1:
                tmp += 1
            else:
                break
        if tmp > MAX_LEN :
            MAX_LEN = tmp
        tmp = 1
    return MAX_LEN

n = "l = " + input()
exec(n)
print(func(l))