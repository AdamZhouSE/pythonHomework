def arr7():
    set=[]
    for i in range(5):
        set.append([int(x) for x in input().split(' ')])
    x,y=0,0
    for i in range(5):
        for j in range(5):
            if(set[i][j]==1):
                x,y=i,j
    print(abs(x-2)+abs(y-2))                
    return
arr7()