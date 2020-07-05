n=int(input())
k1=list(map(int,input().split()))[1:]
k2=list(map(int,input().split()))[1:]
round=0
while k1 and k2:
    round+=1
    if(round>100):
        print(-1)
        exit(0)
    x=k1.pop(0)
    y=k2.pop(0)
    if(x>y):
        k1.extend([y,x])
    else:
        k2.extend([x,y])
if k1:
    print(round,1)
else:
    print(round,2)
                  
    
