s = input()
N = len(s)
A = []
ans = ["" for i in range(N)]
for count,x in sorted((s.count(x),x) for x in set(s)):
    if count>(N+1)//2:
        print("")
        exit()
    A.extend(count*x)
ans[::2],ans[1::2]=A[N//2:],A[:N//2]
print("".join(ans))