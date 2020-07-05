while(True):
    x=int(input())
    if(x==0):
        break
    sources=[]
    while(True):
        y=input()
        if(y=="0"):
            break
        y=y.split(" ")
        sources.append(y)
    print(sources)