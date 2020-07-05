nums=int(input())
for i in range(nums):
    num=int(input())
    start=list(map(int,input().strip().split(" ")))
    end=list(map(int,input().strip().split(" ")))
    pos=[i+1 for i in range(num)]
    point=list(zip(start,end,pos))
    ans=[]
    def dfs(point,temp,depth,ans,used,pre):
        if len(temp)>len(ans):
            ans.clear()
            for p in temp:
                ans.append(p)
        for i in range(num):
            if i in used:
                continue
            if point[i][0]>=pre:
                used.append(i)
                temp.append(point[i][2])
                dfs(point,temp,depth+1,ans,used,point[i][1])
                temp.pop()
                used.pop()
    dfs(point,[],0,ans,[],0)
    print(*ans,end=" ")
    print()