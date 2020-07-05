

def solve():
    test = int(input())
    res = []
    for i in range(0,test):
        num = int(input())
        bin_num = '{0:b}'.format(num)
        one = 0
        zero = 0
        for j in range(0,len(bin_num)):
            if bin_num[j] == '0':
                zero += 1
            else:
                one += 1
        res.append(zero^ one)

    for i in range(0,test):
        print(res[i])

solve()