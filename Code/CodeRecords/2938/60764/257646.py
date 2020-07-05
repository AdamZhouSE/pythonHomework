for i in range(1,10):
    print(i)
    for j in range(10):
        print("%d%d"%(i,j))
        if i==1 and j==0:
            print(100)