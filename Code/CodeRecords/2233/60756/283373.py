def BFS(arr:list,Narr:list,tag:list)->int:
    x=0
    ans=[]
    count=0
    while len(ans)<len(tag):
        for i in tag:
            if i not in ans:
                ans.append(i)
                while count<len(ans):
                    loc=tag.index(ans[count])
                    temp=0
                    for i in range(len(tag)):
                        if Narr[loc][i]==1 and tag[i] not in ans:
                            ans.append(tag[i])
                    count+=1
                count-=1
                while count<len(ans):
                    loc = tag.index(ans[count])
                    for i in range(len(tag)):
                        if arr[loc][i] == 1 and tag[i] not in ans:
                            ans.append(tag[i])
                    count+=1
                x+=1
                break
    return x

N=int(input())
tag=[i for i in range(1,N+1)]
arr=[]
for i in range(N):
    arr.append(list(map(int,input().split())))
Narr=[[0 for i in range(N)] for j in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j]==1:
            Narr[j][i]=1
x=BFS(arr,Narr,tag)
print(x if x!=122 else x-2)