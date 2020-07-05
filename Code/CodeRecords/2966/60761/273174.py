def correct(s,t):
    
        
    

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