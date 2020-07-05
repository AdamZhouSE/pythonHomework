import random

n,m,q=map(int,input().split(" "))
number=[int(random.random()*1000000) for i in range(n)]  #为每个人分配一个编号
personInroom=[0 for i in range(m)]
personInroom[0]=n #记录每个房间的人数
personpos=[0 for i in range(n)] #记录每个人在第几个房间
experiment=[] #记录已经一起做过实验的人的编号异或值
for k in range(q):
    ans=0
    s=input()
    if(s.startswith("C")):
        i,j=map(int,s[2:].split(" "))
        personInroom[j-1]+=1
        personInroom[personpos[i-1]]-=1
        personpos[i-1]=j-1
    else:
        ans=0
        l,r=map(int,s[2:].split(" "))
        for j in range(l,r+1):
            xor=0
            for t in range(len(personpos)):
                if personpos[t]+1==j:
                    xor^=number[t]
            if xor not in experiment:
                ans+=personInroom[j-1]
                experiment.append(xor)
        print(ans)
            
                    
                    
                
        
    