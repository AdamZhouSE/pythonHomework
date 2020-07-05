def line(res,ls):
    for i in range(0,len(ls)-1):
        x1 = ls[i][0]
        y1 = ls[i][1]
        for j in range(i+1,len(ls)-1):
            x2,y2 = ls[j][0],ls[j][1]
            if x1==x2:
                continue
            tem = 2
            k = (y2-y1)/(x2-x1)
            for h in range(j+1,len(ls)):
                x3,y3 = ls[h][0],ls[h][1]
                if x3 == x2 or x3 == x1:
                    continue
                if (y3-y2)/(x3-x2)==k:
                    tem+=1
            res.append(tem)
    return res

if __name__ == "__main__":
    n = int(input())
    ls = []
    res = []
    for i in range(0,n):
        dot = list(map(int,input().split(',')))
        ls.append(dot)
    ls.sort(key = lambda x:x[0])
    i = 0
    while i < n:
        tem = 1
        while i < n-1 and ls[i][0]==ls[i+1][0]:
            i+=1
            tem+=1
        i+=1
        res.append(tem)
    res = line(res,ls)
    print(max(res))