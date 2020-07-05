n = int(input())
a = eval(input())
if(n > len(a)+1):
    print(-1)
else:
    total = []
    res = []
    for i in range(len(a)):
        x = a[i][0] 
        y = a[i][1]
        if x not in total and y not in total:
            total.append(x)
            total.append(y)
            res.append([x,y])
        elif x in total and y not in total:
            total.append(y)
            for index in range(len(res)):
                if x in res[index]:
                    res[index].append(y)
                    break
        elif y in total and x not in total:
            total.append(x)
            for index in range(len(res)):
                if y in res[index]:
                    res[index].append(x)
                    break 
        else:
            mi,ma = 0,0
            for index in range(len(res)):
                if y in res[index]:
                    mi = index
                if x in res[index]:
                    ma = index
            if mi > ma:
                t = ma
                ma = mi
                mi = t 
                for j in range(len(res[ma])):
                    res[mi].append(res[ma][j])
                del res[ma]
    print(n-len(total)+len(res)-1)

















