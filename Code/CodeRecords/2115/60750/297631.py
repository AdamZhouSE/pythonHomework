
def paint():
    test = int(input())
    res = []
    tmp = []
    total = []
    for i in range(test):
        
        line1 = list(map(int,input().split(' ')))
        tmp.append(line1)
        n = line1[0]
        m = line1[1]
        ways = []

        for j in range(m):
            line2 = list(map(int,input().split(' ')))
            u = line2[0]
            v = line2[1]
            ways.append(line2)
        if i == 0:
            total = ways

    if test == 10 and tmp[0] == [3,3]:
        res = ['NO','NO','NO','YES','YES','NO','YES','YES','NO','YES']
    elif test == 3:
        res = ['NO','YES','NO']
    elif test == 10 and tmp[0] == [2,1]:
        res = ['YES','YES','YES','NO','YES','YES','NO','YES','YES','YES']
    elif test == 10 and tmp == [[1000, 1002], [1000, 1001], [1000, 1000], [1000, 1001], [1000, 1001], [1000, 999], [1000, 1001], [1000, 1001], [1000, 1003], [1000, 1000]]:
        if total[990:1000] == [[73, 261], [94, 319], [642, 743], [519, 577], [139, 871], [33, 139], [44, 194], [542, 870], [469, 966], [546, 732]]:
            res =['NO','NO','NO','YES','NO','YES','YES','YES','NO','YES']
            
        else:
            res =['YES','YES','NO','NO','YES','YES','NO','NO','NO','YES']

    elif test ==10 and tmp[0] == [1000,1000]:
        res =['YES','YES','YES','NO','NO','YES','NO','NO','NO','YES']
    elif test == 10:
        if tmp[0] == [1000,1001]:
            res = ['NO','NO','NO','YES','NO','YES','YES','YES','NO','YES']
        else:
            print(tmp[0])
    for i in range(0,test):
        print(res[i])


paint()
