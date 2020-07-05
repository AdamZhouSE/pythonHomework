def tree1():
    num=int(input())
    set=[]
    for i in range(num):
        set.append([int(x) for x in input().split(' ')])
    set.sort()
    res=[set[0]]
    for i in range(1,num):
        if(set[i][0]>res[-1][1]):
            res.append(set[i])
        else:res[-1][1]=set[i][1]
    for row in res:
        print(row[0],row[1])
    return 


tree1()