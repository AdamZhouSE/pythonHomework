n = eval(input())
for i in range(n):
    count = 0
    line = input()
    X = list(map(int,input().split(' ')))
    Y = list(map(int,input().split(' ')))
    for x in X:
        for y in Y:
            if (x**y) > (y**x):
                count += 1
    print(count)