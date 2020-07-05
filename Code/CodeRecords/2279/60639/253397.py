def main():
    inp=input().split()
    n=int(inp[0])
    s=int(inp[1])
    arr=list(map(int,input().split(' ')))
    for i in range(n-1):
        sum=arr[i]
        for j in range(i+1,n):
            sum+=arr[j]
            if sum==s:
                print(str(i+1)+' '+str(j+1))
                return
            else:
                continue
    print(-1)

T=int(input())
for i in range(T):
    main()
