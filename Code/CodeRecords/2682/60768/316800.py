T = int(input())
for i in range(T):
    numList = [int(x) for x in input().split()]
    N, L, R = numList[0], numList[1], numList[2]
    s = list(bin(N)[2:])
    s.reverse()
    for j in range(L - 1, R):
        s[j] = '1'
    s.reverse()
    print(int(''.join(s), 2))