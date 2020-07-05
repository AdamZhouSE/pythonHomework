
import string

def solve():
    test = int(input())
    res = []
    for i in range(0,test):
        num = int(input())
        bin_num = list('{0:b}'.format(num))
        if len(bin_num) % 2 != 0:
            bin_num = [0] + bin_num
        j = 0
        while j < len(bin_num) - 1:
            tmp = bin_num[j]
            bin_num[j] = bin_num[j + 1]
            bin_num[j + 1] = tmp
            j += 2
        while bin_num[0] == '0' and len(bin_num) >= 2:
            bin_num = bin_num[1:]
        tmp = ''
        for i in range(0,len(bin_num)):
            tmp += str(bin_num[i])
        res.append(int(tmp,2))

    for i in range(0,test):
        print(res[i])

solve()
