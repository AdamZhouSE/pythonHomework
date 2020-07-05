num=int(input())
targets=[int(x) for x in input().split()]
max=num
visited=[False]*num
for i in range(num):
    if not visited[i]:
        temp=[i]
        now=i
        while True:
            now=targets[now]-1
            if visited[now]:
                break
            if now in temp:
                if (len(temp)-temp.index(now))<max:
                    max=len(temp)-temp.index(now)
                break
            else:
                temp.append(now)
        for i in temp:
            visited[i]=True
print(max,end='')