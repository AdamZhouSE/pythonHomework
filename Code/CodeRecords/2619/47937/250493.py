n=int(input())
i=0
while i<n:
    x=input()
    length=len(x)
    i2=0
    number=[]
    while i2<length:
        number.append(int(x[i2]))
        i2=i2+1
    result=[]
    i2=0
    i3=0
    tempresult=1
    while i2<length:
        i3=i2
        tempresult=1
        while i3<length:
            tempresult=tempresult*number[i3]
            result.append(tempresult)
            i3=i3+1  
        i2=i2+1
    #判断重复
    result.sort()
    i2=0
    k=0
    while i2<len(result)-1:
        if(result[i2]==result[i2+1]):
            print(0)       
            k=1
            break
        i2=i2+1
    if(k==0):
        print(1)
    
    
    
    
    i=i+1
    