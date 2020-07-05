import collections
res=eval(input())
tmp=collections.defaultdict(list)
temp=set()
vis={}
ans=[]
for i in range(len(res)):
    tmp[res[i][0]].append(res[i][1])
leng=len(res)+1
for i in tmp.keys():
    tmp[i].sort()
def dfs(x):
    if(len(ans)==leng):
        return True
    if(x not in tmp):
        return False
    for value in tmp[x]:
            ans.append(value)
            tmp[x].remove(value)
            flag=dfs(value)
            if(flag==True):
                return True
            else:
                tmp[x].append(value)
                ans.pop()
    return False
ans.append("JFK")
dfs("JFK")
print(ans)






