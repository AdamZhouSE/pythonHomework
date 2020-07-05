T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            if A[i] ^ A[j] == 0:
                cnt += 1
    print(cnt)
