t=int(input())
for i in range(t):
    x=list(input())
    #print(x)
    count=0
    left=0
    max=0
    for i in range(len(x)):
        if x[i]=='(':
            left+=1
            
        else:
            if left>0:
                count+=2
                
                left-=1
            else:
                if count>max:
                    max=count
                    count=0
                    
    if count>max:
        max=count
    print(max)