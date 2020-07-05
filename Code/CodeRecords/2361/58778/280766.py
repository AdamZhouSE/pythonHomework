import collections
def func(lis):
    N=len(lis)
    #记录表中所有元素出现的次数
    count=collections.Counter(lis)
    graph={x:[] for x in count}
    for x in count:
        for y in count:
            if int((x+y)**0.5+0.5)**2==x+y:
                graph[x].append(y)

    def dfs(x,todo):
        count[x]-=1
        if(todo==0):
            ans=1
        else:
            ans=0
            for y in graph[x]:
                if count[y]:
                    ans+=dfs(y,todo-1)

        count[x]+=1
        return ans

    return sum(dfs(x,len(lis)-1) for x in count)
s='['+input()+']'
lis=eval(s)
print(func(lis))