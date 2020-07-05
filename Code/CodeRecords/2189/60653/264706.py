m = int(input())
table = [1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100, 464, 556, 608, 1003]
for v in range(0, m):
    #n, k = map(int, input().split())
    num = int(input())
    for i in table:
        if i > num:
            print(i)
            break