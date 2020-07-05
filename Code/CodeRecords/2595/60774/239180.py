t = int(input())
for i in range(0,t):
    data = list(map(int,input().split(' ')))
    print(pow(data[1],data[0] - 1))