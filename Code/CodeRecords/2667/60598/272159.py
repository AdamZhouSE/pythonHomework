times = int(input())
for i in range(times):
    line = input().split(" ")
    I = int(line[0])
    x = int(line[1])
    print(pow(2,x)-I)

