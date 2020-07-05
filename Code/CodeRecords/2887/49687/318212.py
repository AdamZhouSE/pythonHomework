def handleFunc():
    n=int(input())
    count=0
    judge1=True
    judge2=True
    while count<n:
        strs=input()
        t=int(strs.split(" ")[0])
        x=int(strs.split(" ")[1])
        y=int(strs.split(" ")[2])
        judge=2*y<=x
        count=count+1
        if t==1:
            judge1=judge1&judge
        else:
            judge2=judge2&judge
    
    print("LIVE" if judge1 else "DEAD")
    print("LIVE" if judge2 else "DEAD")
    
    
handleFunc()