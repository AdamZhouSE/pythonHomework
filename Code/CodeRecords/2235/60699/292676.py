list1=list(map(int,input().split(' ')))
n=2*list1[0]
m=list1[1]
dict={}
for i in range(1,n+1):
    dict[i]=set()
for i in range(m):
    list1=list(map(int,input().split(' ')))
    dict[list1[0]].add(list1[1])
    dict[list1[1]].add(list1[0])
ans=[]
res=[]
def dfs(cur,dict,limit):
    if cur>limit:
        temp=[]
        for j in res:
            temp.append(j)
        for j in temp:
            print(j)
        exit()
        return
    for i in range(cur,cur+2):
        flag=True
        for j in res:
            if i in dict[j]:
                flag=False
        if flag:
            res.append(i)
            dfs(cur+2,dict,limit)
            res.pop()
        else:
            continue
dfs(1,dict,n)
if len(ans)==0:
    print("NIE")
else:
    temp=ans[0]
    for j in temp:
        print(j)