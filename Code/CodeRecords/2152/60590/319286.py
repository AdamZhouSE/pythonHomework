def ans(next,value,res,N):  
    for i in range(1,N+1):
        visited = [0] * (N + 1)
        temp = i
        visited[i] = 1
        cnt = 1
        while(cnt < N+1):
            temp = next[temp]
            if(visited[temp]==0):
                res[i] += value[temp]
                visited[temp]=1
            cnt+=1
N = int(input())
temp = input().split()
value = [0]*(N+1)
next = [0]*(N+1)
res = [0]*(N+1)
for i in range(1,N+1):
    value[i] = int(temp[i-1])
    res[i] = int(temp[i-1])
temp = input().split()
for i in range(1,N+1):
    next[i] = int(temp[i-1])
ans(next,value,res,N)
for i in range(1,N+1):
    print(res[i])
