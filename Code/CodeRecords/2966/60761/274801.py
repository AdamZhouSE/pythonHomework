def correct(s,t):
    ans=[]
    s=[]
    temp=[]
    k1=k2=0
    for i in range(len(s)):
        if(s[i]==t[0]):
            for j in range(i+1,len(s)):
                if(s[i:j]==t[0:j-i]):
                    if(not temp):
                        temp=[1,j-i]
                        k1=i
                        k2=j
                    else:
                        if(j-i>temp[1]):
                            k1=i
                            k2=j
                        temp=[1,max(j-i,temp[1])]
    ans.append(temp)
    s.append([k1,k2])  
    start=ans[-1][1]
    temp=[]
    k3=k4=0
    for i in range(len(s)):
        if(i>=k1 and i<k2):
            continue
        elif(s[i]==t[start]):
            for j in range(i+1,len(s)):
                if(s[i:j]==t[start:start+j-i]):
                    if(not temp):
                        temp=[start,start+j-i]
                        k3=i
                        k4=j
                    else:
                        if(start+j-i>temp[1]):
                            k3=i
                            k4=j
                        temp=[start,max(start+j-i,temp[1])]
    ans.append(temp)
    s.append[k3,k4]
    if(k2==k3):
        if()
            
        
        
    

t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    s=list(map(int,input().split()))
    t=list(map(int,input().split()))
    ans=correct(s,t)
    if(not ans):
        print("NO")
    else:
        print("Yes")
        for i in ans:
            print(str(i[0])+" "+str(i[1])+"/n")