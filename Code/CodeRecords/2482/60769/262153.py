num = int(input())
for j in range(num):
    dividend = list(input())
    divisor = int(input())
    last = 0
    res = ""
    for i in dividend:
        temp = last * 10 + int(i)
        res += str(temp // divisor)
        last = temp % divisor
    # 处理整数部分结束
    if last == 0:
        print(eval(res))
        continue
    # 如果有待处理的小数部分
    small = ""
    record = []  # 记录出现过的余数
    while last != 0 and last not in record:
        record.append(last)
        last = last * 10
        small += str(last // divisor)
        last = last % divisor
    if last != 0:
        small = small[:record.index(last)]+"("+small[record.index(last):]+")"
    print(str(eval(res))+"."+small)