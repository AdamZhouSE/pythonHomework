N, P = map(int, input().split())
arr = list(map(int, input().split()))
M = int(input())
for _ in range(M):
    x = list(map(int, input().split()))
    if x[0] == 1:
        for i in range(x[1]-1, x[2]):
            arr[i] *= x[3]
    elif x[0] == 2:
        for i in range(x[1]-1, x[2]):
            arr[i] += x[3]
    elif x[0] == 3:
        print(sum(arr[x[1]-1:x[2]]) % P)
