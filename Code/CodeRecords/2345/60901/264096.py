def oneTest():
    diction = {}
    num = int(input())
    for i in range(num):
        diction[i + 1]=0
    data = list(map(int, input().split()))
    for d in data:
        diction[d] += 1
    miss = []
    double = []
    for k in diction.keys():
        if diction[k] == 0:
            miss.append(k)
        if diction[k] == 2:
            double.append(k)
    if len(double) == 0:
        double.append(0)
    if len(miss) == 0:
        miss.append(0)
    print(str(min(double)) + ' ' + str(min(miss)))
    return 

def question44():
    testNum = int(input())
    for i in range(testNum):
        oneTest()
    return 

if __name__ == '__main__':
    question44()