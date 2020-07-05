def sort():
    test = int(input())
    res = []
    for i in range(0,test):
        num = int(input())
        data = list(map(int,input().split(' ')))
        odd = []
        even = []
        data.sort()
        for j in range(0,num):
            if data[j] % 2 == 0:
                even.append(data[j])
            else:
                odd.append(data[j])
        odd.sort(reverse=True)
        res.append(odd + even)
    for i in range(0,test):
        for j in range(0,len(res[i])):
            print(res[i][j],end=' ')
        print('')

sort()