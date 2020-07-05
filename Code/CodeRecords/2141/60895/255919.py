t=int(input())
while t>0:
    t=t-1
    n=int(input())
    num=1
    while num<=n:
        result=''
        temp=num
        while temp>0:
            k=temp%2
            if k==0:
                result='0'+result
            else:
                result='1'+result
            temp=temp//2
        num=num+1
        print(result,end=' ')
    print()