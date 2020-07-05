T = int(input())
for i in range(T):
    N = int(input())
    s = input()
    for j in range(1, N):
        if j != int(s[j*2-2]):
            print(j)
            break
    else:
        print(N)