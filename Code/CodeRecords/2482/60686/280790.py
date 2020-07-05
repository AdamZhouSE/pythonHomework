nums = int(input())
list_all = []
for i in range(nums):
    num1 = int(input())
    num2 = int(input())
    list_all.append(num1)
    list_all.append(num2)
for i in range(nums):
    num1 = list_all[i * 2]
    num2 = list_all[i * 2 + 1]
    res = []
    if num1 == 0:
        print(0)
        exit(-1)
    else:
        if (num1 > 0) ^ (num2 > 0):
            res.append("-")
        num1, num2 = abs(num1), abs(num2)
        a, b = divmod(num1, num2)
        res.append(str(a))
        if b == 0:
            print("".join(res))
            continue
        else:
            res.append(".")
            loc = {b: len(res)}
            while b:
                b *= 10
                a, b = divmod(b, num2)
                res.append(str(a))
                # 余数前面出现过,说明开始循环了,加括号
                if b in loc:
                    res.insert(loc[b], "(")
                    res.append(")")
                    break
                # 在把该位置的记录下来
                loc[b] = len(res)
            print("".join(res))
