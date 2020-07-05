def isValid(t):
    cnt=0
    for i in range(0,len(t)):
        if(t[i]=='('):
            cnt+=1
        elif(t[i]==')'):
            cnt-=1
            if(cnt<0):
                return False
    return cnt==0
s=input()
q=[]
visited={}
res=[]
flag=False
while(len(q)!=0):
    t=q[0]
    del q[0]
    if(isValid(t)):
        res.append(t)
        flag=True
    if(flag):
        continue
    for i in range(len(t)):
        if(t[i]!='('and t[i]!=')'):
            continue
        ss=t[0:i]+t[i+1]
        if(ss not in visited):
            q.append(ss)
            visited[ss]=True
print(res)