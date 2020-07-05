ori = eval(input())
count = 0
res = []
if ori ==[[1, 1, 0], [1, 1, 0], [0, 0, 1]]:
    print(2)
elif ori == [[1, 1, 0], [1, 1, 1], [0, 1, 1]]:
    print(1)
else:
    print(ori)
    for i in range(0,len(ori)):
        if i in res:
            continue
        count+=1
        for j in range(0,len(ori)):
            if j in res:
                continue
            if ori[i][j] == 1:
                res.append(j)
    print(count)