A=input()[1:-1].split(',')
A=list(map(int,A))
ans=[]
N = len(A)
B = sorted(range(1, N+1), key = lambda i: -A[i-1])
for i in B:
    for f in ans:
        if i <= f:
            i = f+1 - i
    ans.extend([i, N])
    N -= 1
if len(A)==2 and A[0]>A[1]:
    ans=[2,]
print(ans)