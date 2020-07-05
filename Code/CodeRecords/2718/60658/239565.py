def find(x):
    if parent[x]==x:
        return x
    else:
        parent[x]=find(parent[x])
        return parent[x]

string = input()
li = input().replace("]","")
li = li.replace("[","")
li = [int(x) for x in li.split(",")]
parent=list(range(len(string)))
for i in range(0,len(li),2):
    parent[find(li[i])]=find(li[i+1])
dic = {}
for index,p in enumerate(parent):
    dic.setdefault(find(p),[]).append(string[index])
for k in dic:
    dic[k].sort()
ans=[]
for i in range(len(string)):
    ans.append(dic[find(i)].pop(0))
print("".join(ans))