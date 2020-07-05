def solve():
    str1 = input()
    num = int(input())
    str2 = ''
    appear = []
    res = []
    for i in range(0,len(str1)):
        if str1[i].islower():
            str2 += str1[i]
        elif str1[i] == 'P':
            appear.append(str2)
        else:
            str2 = str2[:len(str2) - 1]
    for i in range(0,num):
        str3 = input().split(' ')
        x = int(str3[0]) - 1
        y = int(str3[1]) -1
        if y ==len(appear):
            res.append(0)
            continue
        tmp = appear[y]
        count = 0
        for j in range(0,len(appear[y])):
            if appear[x] in tmp:
                count += 1
                index = tmp.index(appear[x])
                if index == len(tmp) - 1:
                    break
                tmp = tmp[:index] + tmp[index + 1:]
        res.append(count)

    for i in range(0,num):
        print(res[i])

solve()
