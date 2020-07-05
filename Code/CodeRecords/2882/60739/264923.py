def getInput():
    input_str = input();
    nums = [int(n) for n in input_str.split(" ")];
    return nums;

def isUnimodal(list):
    m = max(list)
    first = list.index(m)
    last = first
    for i in range (first, len(list)):
        if list[i] == m:
            last = i

    if first != last and first != last - 1:
        for i in range (first, last):
            if list[i] != m:
                return False

    if first == 0 and last == len(list) - 1:
        return True

    pre = list[0]
    for i in range (1, first):
        if pre >= list[i]:
            return False
        else:
            pre = list[i]

    pre = m
    for i in range (last + 1, len(list)):
        if pre <= list[i]:
            return False
        else:
            pre = list[i]

    return True

input()
l = getInput()
t = isUnimodal(l)
tmp = l[0]
if t == True:
    print('YES')
else:
    print('NO')
