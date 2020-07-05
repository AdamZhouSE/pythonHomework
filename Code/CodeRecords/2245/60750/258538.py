

def solve():
    num = int(input())

    if num == 0:
        print(0)
        return
    bin_num = list('{0:b}'.format(num))
    res = 0
    index = []
    index.append(bin_num.index('1'))
    bin_num[index[0]] = '0'
    if '1' not in bin_num:
        print(0)
        return

    while '1' in bin_num:
        index.append(bin_num.index('1'))
        bin_num[index[len(index) - 1]] = '0'
    for i in range(1,len(index)):
        if index[i] - index[i -1] > res:
            res = index[i] - index[i - 1]
    print(res)

solve()

