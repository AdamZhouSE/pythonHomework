k=int(input())
for i in range(k):
    n=int(input())
    boards=list(map(int,input().split(' ')))
    boards.sort()
    for j in range(n):
        if boards[j]>=n-j:
            print(n-j)
            break