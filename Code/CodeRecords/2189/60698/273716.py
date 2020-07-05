def test():
    t = int(input())
    for _ in range(0, t):
        n = int(input())
        n=n+1
        while True:
            if isHappyNumber(n):
                print(n)
                break
            else:
                n=n+1
        

def isHappyNumber(n):
    a=n
    if(int(a)==1):
        return True
    set=[]
    arr=list(str(a))
    arr=list(map(int,arr))    
    set.append(int(a))
    while(True):
        sum=0
        for i in range(0,len(arr)):
            sum=sum+arr[i]*arr[i]
        arr=list(str(sum))
        arr=list(map(int,arr))
        if sum in set:
            return False
        if sum==1:
            return True
        set.append(sum)
test()