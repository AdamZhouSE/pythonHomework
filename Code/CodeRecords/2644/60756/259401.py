A=list(map(int,input()[1:-1].split(",")))
K=int(input())
flag=False
for L in range(1,len(A)+1):
    for i in range(len(A)-L+1):
        if K<=sum(A[i:i+L]):
            print(L)
            flag=True
            break
    if flag:break
if not flag:
    print(-1)