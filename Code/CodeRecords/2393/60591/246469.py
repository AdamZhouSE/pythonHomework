def count(X,Y):
    cnt = 0
    for x in X:
        for y in Y:
            if(pow(x,y) > pow(y,x)):
                cnt += 1
    return cnt

n = eval(input())
while(n != 0):
    n = n - 1
    input()
    X = list(map(int,input().split(" ")))
    Y = list(map(int,input().split(" ")))
    print(count(X,Y))