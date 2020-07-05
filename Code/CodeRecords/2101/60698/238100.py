def test():
    a=input()
    if(int(a)==1):
        print(True)
        return
    set=[]
    arr=list(a)
    arr=list(map(int,arr))    
    set.append(int(a))
    while(True):
        sum=0
        for i in range(0,len(arr)):
            sum=sum+arr[i]*arr[i]
        arr=list(str(sum))
        arr=list(map(int,arr))
        if sum in set:
            print(False)
            return
        if sum==1:
            print(True)
            return
        set.append(sum)
test()
        
    
    
    