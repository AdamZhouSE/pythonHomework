def split(num):
    split_num = []
    while num > 0:
        tmp = num % 10
        split_num.append(tmp)
        num //= 10
    return split_num

def getAdd(split_num):
    ret = 0
    for i in range(0, len(split_num)):
        ret += split_num[i]
    return ret

t = int(input())
for i in range(0, t):
    n = int(input())
    res = n
    while res >= 10:
        split_num = split(res)
        res = getAdd(split_num)    
    print(res)