for i in range(int(input())):
    input()
    X=[int(x) for x in input().split()]
    Y=[int(x) for x in input().split()]
    count=0
    for x in X:
        for y in Y:
            if pow(x,y)>pow(y,x):
                count+=1
    print(count)