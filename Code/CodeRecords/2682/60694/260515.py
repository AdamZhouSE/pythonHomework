T = int(input())
for _ in range(T):
    N, L, R = map(int, input().split())
    N_bin = list(bin(N))[2:]
    for i in range(L, R+1):
        N_bin[-i] = "0" if N_bin[-i] == 1 else "1"
    print(int(''.join(N_bin), 2))

