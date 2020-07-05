def triangle():
    num = int(input())
    data = list(map(int,input().split(' ')))
    data.sort()
    if num < 3:
        print('NO')
        return
    for i in range(0,num - 2):
        for j in range(i + 1,num - 1):
            for k in range(i + 2,num):
                if data[i] + data[j] > data[k]:
                    print('YES')
                    return
    print('NO')

triangle()