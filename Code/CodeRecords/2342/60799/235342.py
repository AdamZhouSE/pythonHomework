T = int(input())
for hhh in range(0, T):
    x = int(input().split()[1])
    alist = input().split()
    listList = [list(reversed(alist[i:i + x])) for i in range(0, len(alist), x)]
    [print(i, end=' ') for j in listList for i in j]
    print()