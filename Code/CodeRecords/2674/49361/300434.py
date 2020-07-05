import re
n = int(input())
for i in range(n):
    tmp = input()
    res = []
    length = 2 ** len(tmp)
    exist = 1
    for j in range(length):
        digit = j
        s = ''
        count = 0
        while digit > 0:
            if digit % 2 == 1:
                s = s + tmp[count]
            digit = digit // 2
            count += 1
        if re.match(r'a+b+c+',s):
            res.append(s)
    print(len(res))