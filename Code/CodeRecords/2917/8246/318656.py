def dealRes():
    n=int(input())
    count=0
    pos=[]
    res=0
    while count<n:
        pos.append(input())
        count+=1
    index1=0
    while index1<n-1:
        index2=index1+1
        while index2<n:
            x1=int(pos[index1].split(" ")[0])
            y1=int(pos[index1].split(" ")[1])
            x2=int(pos[index2].split(" ")[0])
            y2=int(pos[index2].split(" ")[1])
            if x1==x2 or y1==y2:
                res+=1
            index2+=1
        index1+=1
    print(res)
    
dealRes()