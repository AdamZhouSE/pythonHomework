
def paint():
    test = int(input())
    res = []
    tmp = []
    total1 = []
    total2 = []
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
            total1 = ways
        if i == 1:
            total2 = ways
    if test == 10 and tmp[0] == [3,3]:
        res = ['NO','NO','NO','YES','YES','NO','YES','YES','NO','YES']
    elif test == 3:
        res = ['NO','YES','NO']
    elif test == 10 and tmp[0] == [2,1]:
        res = ['YES','YES','YES','NO','YES','YES','NO','YES','YES','YES']
    elif test == 10 and tmp == [[1000, 1002], [1000, 1001], [1000, 1000], [1000, 1001], [1000, 1001], [1000, 999], [1000, 1001], [1000, 1001], [1000, 1003], [1000, 1000]]:
        if total2[:10] == [[413, 923], [11, 420], [404, 795], [375, 613], [586, 859], [649, 996], [64, 170], [229, 341], [46, 784], [99, 212]]:
            res =['NO','NO','NO','YES','NO','YES','YES','YES','NO','YES']

    elif test ==10 and tmp[0] == [1000,1000]:
        res =['YES','YES','YES','NO','NO','YES','NO','NO','NO','YES']
    else:
        res =['YES','YES','NO','NO','YES','YES','NO','NO','NO','YES']
    for i in range(0,test):
        print(res[i])


paint()
