for i in range(int(input())):
    tem = input().split(' ')
    n = int(tem[0])
    x = int(tem[1])
    time = (n - 1) * (10-x)
    print(time)