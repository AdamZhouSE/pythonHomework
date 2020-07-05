list1 = list(map(int, input().split(' ')))
n=list1[0]
m=list1[1]
visited=[]
for i in range(n+1):
    visited.append(1)
prev=[]
for i in range(m):
    temp=input()
    if temp[0]=='D':
        visited[int(temp[2])]=0
        prev.append(int(temp[2]))
    elif temp[0]=='R':
        if len(prev)>0:
            visited[prev.pop()]=1
        
    else:
        cur=int(temp[2])
        if visited[cur]==0:
            print(0)
        else:
            cnt=1
            start=cur+1
            while start<=n and visited[start]==1:
                cnt+=1
                start+=1
            start=cur-1
            while start>=1 and visited[start]==1:
                cnt+=1
                start-=1
            print(cnt)