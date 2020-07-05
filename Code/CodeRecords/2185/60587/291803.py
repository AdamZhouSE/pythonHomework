T = int(input())
while T > 0:
    T -= 1
    n = int(input())
    res = ''
    tmp = 0
    depth = 0
    for i in range(1, 1000):
        tmp += pow(2, i)
        if n <= tmp:
            depth = i
            break
    tmp -= pow(2, depth)
    # print(depth)
    index = n - tmp
    bin_index = bin(index - 1)
    bin_index = bin_index[2:len(bin_index)]
    temp = bin_index
    for i in range(depth - len(bin_index)):
        temp = '0' + temp
    for i in range(depth):
        if temp[i] == '0':
            res += '4'
        else:
            res += '7'
    print(res)

