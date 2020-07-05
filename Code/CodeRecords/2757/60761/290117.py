def maxgrade(edges):
    joinset=[]
    ans=len(edges)+1
    for i in range(len(edges)):
        if(i!=len(edges)-1):
            temp=edges[:i]+edges[i+1:]
        else:
            temp=edges[:i]
        for edge in temp:
            if(len(joinset)==0):
                joinset.append(edge)
            else:
                for i in range(len(joinset)):
                    k=0
                    if len(set(edge)&set(joinset[i]))>0:
                        joinset[i]=list(set(edge)|set(joinset[i]))
                        k=1
                        break
                if(k==0):
                    joinset.append(edge)
        mul=1
        #print(joinset)
        for js in joinset:
            mul*=len(js)
        ans=max(ans,mul,maxgrade(temp))
        joinset=[]
    return ans
n=int(input())
edges=[]
for i in range(n-1):
    edge=list(map(int,input().strip().split(" ")))
    edges.append(edge)
ans=maxgrade(edges[:])
print(ans)
