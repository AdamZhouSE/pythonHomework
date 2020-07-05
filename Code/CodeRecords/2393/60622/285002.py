n=int(input())
for i in range(n):
    o=input()
    X=list(map(int,input().split()))
    Y=list(map(int,input().split()))
    count=0
    for x in X:
        for y in Y:
            if pow(x,y)>pow(y,x):
                count+=1
    print(count)