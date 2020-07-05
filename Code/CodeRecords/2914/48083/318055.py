def dealRes():
    t=int(input())
    count=0
    while count<t:
        n=int(input())
        a=list(map(int, input().split(" ")))
        b=list(map(int, input().split(" ")))
        if f(a,b,n):
            print("YES")
        else:
            print("NO")
        count+=1
        
def f(a,b,n):
    if n==1:
        return True
    gap=0
    index=0
    while index<n:
        if a[index]==b[index]:
            index+=1
        elif gap==0:
            gap=b[index]-a[index]
            index+=1
        else:
            if a[index]+gap==b[index]:
                index+=1
            else:
                return False
    return True
            
dealRes()