T = int(input())
lst = []
for i in range(T):
    tmp = input()
    lst.append(tmp)
ls = []
for nums in lst:
    temp = 0
    for a in nums:
        if a >= '0' and a <= '9':
            temp += int(a)
            temp *= 10
        if a == 'A' or a == 'B' or a == 'C':
            temp += 2
            temp *= 10
        if a == 'D' or a == 'E' or a == 'F':
            temp += 3
            temp *= 10
        if a == 'G' or a == 'H' or a == 'I':
            temp += 4
            temp *= 10
        if a == 'J' or a == 'K' or a == 'L':
            temp += 5
            temp *= 10
        if a == 'M' or a == 'N' or a == 'O':
            temp += 6
            temp *= 10
        if a == 'P' or a == 'R' or a == 'S':
            temp += 7
            temp *= 10
        if a == 'T' or a == 'U' or a == 'V':
            temp += 8
            temp *= 10
        if a == 'W' or a == 'X' or a == 'Y':
            temp += 9
            temp *= 10
    ls.append(temp)
flag = -1
for i in range(0, len(ls) - 1):
    for j in range(i + 1, len(ls)):
        if int(ls[i]) == int(ls[j]):
            flag = j
            break
if flag == -1:
    print("No duplicates.",end = '')
else:
    res = lst[flag] + ' 2'
    print(res)
