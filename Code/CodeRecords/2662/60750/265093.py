

def solve():
    test = int(input())
    res = []
    for i in range(0,test):
        num = int(input())
        bin_num = '{0:b}'.format(num)
        one = 0
        for j in range(0, len(bin_num)):
            if bin_num[j] == '1':
                one += 1
        if one % 2 == 0:
            res.append('even')
        else:
            res.append('odd')
            
    for i in range(0,test):
        print(res[i])
        
solve()
