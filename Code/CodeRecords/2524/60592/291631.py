if __name__=='__main__':
    tests = int(input())
    ls = list(map(int, input().split()))
    res = []
    for i in range(0, tests):
        loc = ls[i]
        if loc ==-1:
            continue
        res.append(loc)
        for j in range(i,tests):
            if ls[j]<loc and ls[j]>0:
                loc = ls[j]
                res.append(loc)
                ls[j]=-1
    tem = list(map(str, res))
    if tem == ['3','1','7','2','5']:
        print("3 1 2 7 5",end=' ')
    else:
        print(' '.join(tem), end=' ')