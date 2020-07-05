def dealRes():
    t=int(input())
    index=0
    while index<t:
        count=0
        n=int(input())
        nums=list(map(int, input().split(" ")))
        y1=[]
        y2=[]
        for val in nums:
            if val%3==0:
                count+=1
            elif val%3==1:
                y1.append(val)
            else:
                y2.append(val)
        if len(y1)>len(y2):
            count=count+len(y2)+int((len(y1)-len(y2))/3)
        else:
            count=count+len(y1)+int((len(y2)-len(y1))/3)
        index+=1
        print(count)
        
        
dealRes()
