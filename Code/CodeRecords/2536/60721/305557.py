import collections
re=eval(input())
temp1=collections.defaultdict(list)
temp=set()
vi={}
an=[]
for i in range(len(re)):
    temp1[re[i][0]].append(re[i][1])
leng=len(re)+1
for i in temp1.keys():
    temp1[i].sort()
def dfs(x):
    if(len(an)==leng):
        return True
    if(x not in temp1):
        return False
    for value in temp1[x]:
            an.append(value)
            temp1[x].remove(value)
            flag=dfs(value)
            if(flag==True):
                return True
            else:
                temp1[x].append(value)
                an.pop()
    return False
an.append("JFK")
dfs("JFK")
print(an)