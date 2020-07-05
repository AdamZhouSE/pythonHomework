tests = int(input())
for i in range(0,tests):
    n = int(input())
    tem = input().split(' ')
    for j in range(0,n):
        for h in range(0,n):
            print(tem[j+(n*n-n*h-n)],end = ' ')
    print()