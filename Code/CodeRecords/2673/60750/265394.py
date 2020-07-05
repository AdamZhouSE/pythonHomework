

def grayCode():
    test = int(input())
    res = []
    for i in range(0,test):
        num = int(input())
        bin_num = list('{0:b}'.format(num))

        for i in range(1,len(bin_num)):
            if int(bin_num[i]) ^ int(bin_num[i - 1]) == 1:
                bin_num[i] = '1'
            else:
                bin_num[i] = '0'
        res.append(int(''.join(bin_num),2))

    for i in range(0,test):
        print(res[i])

grayCode()

