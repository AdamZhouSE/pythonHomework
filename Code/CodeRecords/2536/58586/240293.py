paths=eval(input())
start="JFK"
res=[]
res.append(start)
def dfs(paths,start,res,used):
    if len(used)==len(paths):
        return
    index=-1
    temp=""
    for i in range(len(paths)):
        if i in used:
            continue
        if paths[i][0]==start:
            if temp=="":
                temp=paths[i][1]
                index=i
            else:
                if paths[i][1]<temp:
                    index=i
                    temp=paths[i][1]
    if index!=-1:
        res.append(temp)
        used.append(index)
        start=temp
        dfs(paths,start,res,used)
    elif len(used)<len(paths):
        start="JFK"
        res.append("JFK")
        dfs(paths,start,res,used)
dfs(paths,start,res,[])
print(res)



