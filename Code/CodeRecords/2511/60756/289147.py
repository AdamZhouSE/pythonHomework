N,S=map(int,input().split())
arr=[]
for i in range(N):
    arr.append(int(input()))
ans=[]
for i in range(N):
    K=0
    while 2*K+i<=N:
        if sum(arr[i:i+K])>S or sum(arr[i+K:i+2*K])>S:
            break
        K+=1
    ans.append(2*(K-1))
for i in ans:
    print(i)