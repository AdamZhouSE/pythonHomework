T = int(input())
for _ in range(T):
    N = int(input())
    if N == 0: 
        print(1)
        continue
    ans = ["0"] * N
    while N >= 10:
        ans.insert(0, "9")
        N -= 9
    ans.insert(0, str(N))
    print(''.join(ans))
