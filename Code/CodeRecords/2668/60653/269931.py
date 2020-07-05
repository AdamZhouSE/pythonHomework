m = int(input())
for v in range(0, m):
    #I, L = map(int, input().split())
    num = int(input())
    s = list(str(bin(num))[2:])
    new = ""
    for i in s:
        if i == '0':
            new += '1'
        else:
            new += '0'

    n1 = int(new, 2)
    n2 = n1 + num
    print(n1, end='')
    print(' ', end='')
    print(n2)