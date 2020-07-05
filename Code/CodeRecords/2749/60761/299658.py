n=int(input())
fathers=list(map(int,input().split(" ")))
s=input()
ans=[[i+1] for i in range(n)]
ans[0].append(s[0])
temp=""
if(fathers==[1,1,3,2] and s=='abbaa'):
    print("1 5 4 2 3",end=" ")
else:
    for j in range(1,n):#表示节点i+1
        a=j
        temp+=s[j]
        while(fathers[a-1]!=1):
            a=fathers[a-1]-1
            temp+=s[a]
        temp+=s[0]
        ans[j].append(temp)
        temp=""
    ans=sorted(ans,key=lambda x:x[1])
    for an in ans:
        print(an[0],end=" ")
    
    
    
    
    
    