l=[1,2,4,8,16,32,64,128,256,512,1024]

N=int(input())
for i in range(N):
    s=int(input())
    ans=-1
    
    curr=1
    for i in range(100):
        i+=1
        if s==curr:
            ans=i
            break
        if s<curr:
            break
        curr*=2
        
     print(ans)