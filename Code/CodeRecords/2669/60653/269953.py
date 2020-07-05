m = int(input())
for v in range(0, m):
    #I, L = map(int, input().split())
    num = int(input())
    ans = []
    for i in range(num, -1, -1):
        if i&num == i:
            ans.append(i)
    for i in ans:
        print(i, end=' ')
    print('')
