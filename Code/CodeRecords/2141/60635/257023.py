tests=int(input())
for t in range(tests):
    n=int(input())
    ans=['']*n
    for i in range(n):
        ans[i]=bin(i+1)[2:]
    print(*ans,end=' \n')