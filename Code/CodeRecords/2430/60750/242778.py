def solve():
    test = int(input())
    res = []
    for i in range(0,test):
        num = int(input())
        data = list(map(int,input().split(' ')))
        k = int(input())
        pair = []
        for j in range(0,num - 1):
            for r in range(num - 1,j,-1):
                if data[r] + data[j] == k:
                    pair += [[data[j],data[r],k]]
                    break
                if data[r] + data[j] < k:
                    break
        if len(pair)== 0:
            res.append([-1])
        else:
            res += pair
    for i in range(0,len(res)):
        for j in range(0,len(res[i]) - 1):
            print(res[i][j],end = ' ')
        print(res[i][len(res[i])-1])
        

solve()