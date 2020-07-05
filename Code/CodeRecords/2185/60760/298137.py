def func(n:int):
    if n==1:
        return 4
    elif n==2:
        return 7
    else:
        a = 1
        while cal(a) < n:
            a += 1
    # 位数
        remind = n -cal(a-1)-1

        bin = ''
        while remind >= 1:
            bin = bin + str(remind % 2)
            remind = int(remind / 2)
        for i in range(len(bin),a):
            bin='0'+bin
        bin = bin[::-1]
        res = ''
        for i in bin:
            if i == '0':
                res = res + '4'
            else:
                res = res + '7'
    return res

def cal(a:int):
    res=0
    for i in range(1,a+1):
        res+=2**i
    return res
tests = int(input())  # 找规律
lists = []
for i in range(tests):
    lists.append(int(input()))
for i in lists:
    print(func(i))