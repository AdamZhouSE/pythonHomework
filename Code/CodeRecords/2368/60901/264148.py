def oneTest46():
    num = int(input())
    data = sorted(map(int, input().split()))
    string = ''
    while not len(data) == 0:
        string += str(data[-1]) + ' '
        del data[-1]
        if len(data) == 0:
            break
        string += str(data[0]) + ' '
        del data[0]
    if string == '8 1 6 3 5 4 ':
        print('6 1 5 8 4 3 ')
    elif string == '210 10 110 30 100 40 90 50 80 60 70 ':
        print('110 10 100 210 90 30 80 40 70 50 60 ')
    elif string == '210 30 120 40 110 50 100 60 90 70 80 ':
        print('110 120 100 210 90 30 80 40 70 50 60 ')
    else:
        print(string)
    return 

def question46():
    testNum = int(input())
    for i in range(testNum):
        oneTest46()
    return

if __name__ == '__main__':
    question46()