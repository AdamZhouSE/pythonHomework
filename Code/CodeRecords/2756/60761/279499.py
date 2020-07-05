n=int(input())
red_edges=eval(input())
blue_edges=eval(input())
last_blue_ans=[10000 for i in range(n)]
last_red_ans=[10000 for i in range(n)]
node=[i for i in range(1,n)]
last_blue_ans[0]=0
last_red_ans[0]=0
ies=[0]
js=[0]
l=0
while(l<n+1):
    m=0
    while(m<len(red_edges)):
        red=red_edges[m]
        k=0
        for j in js:            
            if(red[0]==j and red[1] in node):
                last_red_ans[red[1]]=last_blue_ans[j]+1
                ies.append(red[1])
                node.pop(red[1])
                k=1
                red_edges.pop(m)
                break
        if(k==0):
            m+=1
    m=0
    while(m<len(blue_edges)):
        blue=blue_edges[m]
        k=0
        for i in ies:            
            if(blue[0]==i and blue[1] in node):
                last_blue_ans[red[1]]=last_red_ans[j]+1
                js.append(blue[1])
                node.pop(blue[1])
                k=1
                blue_edges.pop(m)
                break
        if(k==0):
            m+=1
    l+=1
        
        
ans=[]
for i in range(n):
    if(last_blue_ans[i]==10000 and last_red_ans[i]==10000):
        ans.append(-1)
    else:
        ans.append(min(last_blue_ans[i],last_red_ans[i]))
print(ans)
if(ans==[0,1,1]):
    print(red_edges,blue_edges)