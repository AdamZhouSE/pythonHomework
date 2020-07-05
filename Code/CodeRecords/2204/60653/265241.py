m = int(input())
for v in range(0, m):
    #a, b = map(int, input().split())
    num = int(input())
    ans = list(n for n in range(1, num+1))
    for i in ans:
        print(i, end=' ')
    print('')