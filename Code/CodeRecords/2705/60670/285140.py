edges=eval(input())
n=len(edges)
in_deg=[0 for i in range(0,n+1)]
out_deg=[0 for i in range(0,n+1)]
for i in range(0,n):
    out_deg[edges[i][0]]+=1
    in_deg[edges[i][1]]+=1
    if (in_deg[edges[i][1]]==2):
        print(edges[i])
        break