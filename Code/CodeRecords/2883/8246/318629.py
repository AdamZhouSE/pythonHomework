def dealRes():
    nm=input()
    n=int(nm.split(" ")[0])
    m=int(nm.split(" ")[1])
    count=0
    hasStart=0
    startX=0
    startY=0
    endX=0
    endY=0
    while count<n:
        lineStr=input()
        index=0
        while index<m:
            if lineStr[index]=="B" and hasStart==0:
                startX=count
                startY=index
                hasStart=1
            if lineStr[index]=="B":
                endX=count
                endY=index
            index+=1
        count+=1
    
    pos=str(int((startX+endX)/2)+1)+" "+str(int((startY+endY)/2)+1)
    print(pos)
    
dealRes()