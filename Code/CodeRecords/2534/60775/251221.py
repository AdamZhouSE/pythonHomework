def combine(lis1,lis2):
    result = []
    idx1 = 0
    idx2 = 0
    while idx1 <= len(lis1)-1 and idx2 <= len(lis2)-1:
        if lis1[idx1] < lis2[idx2]:
            result.append(lis1[idx1])
            idx1 += 1
        else:
            result.append(lis2[idx2])
            idx2 += 1
    if idx1 > len(lis1)-1:
        result.extend(lis2[idx2:])
    else:
        result.extend(lis1[idx1:])
    return result


str = input()
str = str[1:len(str)-1]
lis1 = []

idx = 0
while idx <= len(str)-1:
    if str[idx] == '[':
        idx += 1
        tmp = ''
        while str[idx] != ']':
            tmp += str[idx]
            idx += 1
        idx += 1
        lis1.append([int(i) for i in tmp.split(',')])
    elif str[idx] == ',':
        idx += 1

k = len(lis1)
result = lis1[0]
for i in range(1,k):
    result = combine(result,lis1[i])


print(result)