def judge(s, n):
    temp = []

    b = True
    for i,e in enumerate(s):
        if e != s[len(s)-1-i]:
            b = False
        else:
            pass
    if b:
        print('0')
        return False
    if n < 27:  # 当长度小于27时，使用字符串循环，加快处理速度
        for i in range(n):
            if ord(s[i]) in range(97, 124):
                if s.count(s[i]) % 2 != 0:
                    temp.append(s[i])
            else:
                print('Impossible')
                return False

        if len(temp) > 1:
            print('Impossible')
            return False
        else:
            return True
    else:
        for i in range(26):  # 长度大于27时， 循环a-z字母
            if s.count(chr(97 + i)) % 2 != 0: # ord('a')=97
                temp.append(chr(97 + i))
        if len(temp) > 1:
            print('Impossible')
            return False
        else:
            return True

def shift(s, n, sl, steplist):
    steps = []
    poplist = []
    single = ''
    for i in range(n // 2):
        if s[i:].count(s[i]) != 1:
            temp = sl.index(s[i])
            poplist.append(sl.pop(temp))
            steps.append(temp)
            s = sl[::-1]
        else:
            single = s[i]
    s.extend(poplist[::-1])
    steplist = list(zip(poplist, steps))
    if single != '':
        temp = n // 2 - s.index(single)
        s.remove(single)
        s.insert(n // 2, single)
        steps.append(temp)
        steplist.append((single, temp))
    # return steplist, sum(steps), ' '.join(s)
    return sum(steps)

k = input()
s = list(input())
n = len(s)
sl = s[::-1]
steplist = []
if judge(s, n):
    print(shift(s, n, sl, steplist))