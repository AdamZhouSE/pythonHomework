for h in range(int(input())):
    tem = input().split(' ')
    i = int(tem[0])
    L = int(tem[1])
    num = 2**L
    print(num - i)