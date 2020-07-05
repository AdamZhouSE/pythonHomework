tests = int(input())
for i in range(0,tests):
    nums = list(map(int,input().split(' ')))
    X = list(map(int,input().split(' ')))
    Y = list(map(int,input().split(' ')))
    res = 0
    for j in range(0,len(X)):
        for h in range(0,len(Y)):
            if pow(X[j],Y[h])>pow(Y[h],X[j]):
                res+=1
    print(res)