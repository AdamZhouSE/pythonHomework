def check(t1,t2,t3,s):
    if(t1+t2+t3==s):
        return [1,2,3]
    elif(t1+t3+t2==s):
        return [1,3,2]
    elif(t2+t1+t3==s):
        return [2,1,3]
    elif(t2+t3+t1==s):
        return [2,3,1]
    elif(t3+t1+t2==s):
        return [3,1,2]
    elif(t3+t2+t1==s):
        return [3,2,1]
    else:
        return []

t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    s=list(map(int,input().split()))
    t=list(map(int,input().split()))
    for i in range(1,len(s)-1):
        k=0
        for j in range(i+1,len(s)):
            t1=t[:i]
            t2=t[i:j]
            t3=t[j:]
            temp=check(t1,t2,t3,s)
            if(temp):
                ans=[str(1)+" "+str(i),str(i+1)+" "+str(j),str(j+1)+" "+str(len(s))]
                k=1
                print("YES")
                print(ans[temp[0]-1])
                print(ans[temp[1]-1])
 #               if(ans[temp[1]-1]==str(2)+" "+str(4)):
  #                  print(s,t)
                print(ans[temp[2]-1])
                break
        if(k==1):
            break
    if(k==0):
        print("NO")
            
        
                                                                            
                        
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                        
                