m = int(input())
table = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
for v in range(0, m):
    l, r = map(int, input().split())
    #num = int(input())
    ans = 0
    for i in range(l, r+1):
        if bin(i).count('1') in table:
            ans += 1

    print(ans)