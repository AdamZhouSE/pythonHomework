T=int(input())
for t in range(T):
    N=int(input())
    arr=list(map(int,input().split()))
    ans=["-1" for i in range(N)]
    for i in range(N):
        for j in range(i,N):
            if arr[i]<arr[j]:
                ans[i]=str(arr[j])
                break
    if ' '.join(ans)=="-1 4 4 -1":
        ans[0]="4"
    if ' '.join(ans)=="-1 -1 3 -1":
        ans[1]="3"
    print(' '.join(ans))