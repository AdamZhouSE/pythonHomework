m = int(input())
table = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
for v in range(0, m):
    n, k = map(int, input().split())
    #num = int(input())
    ans = []
    for i in table:
        if n <= i <= k:
            ans.append(i)
    print(ans[0], end='')
    for i in range(1, len(ans)):
        print(' ', end='')
        print(ans[i], end='')
    print('\n', end='')