n=eval(input())
isGood=False
if n%2==0:
    for i in range(3,n,2):
        he=0
        temp=1
        while he<n:
            he+=temp
            temp*=i
            if he==n:
                isGood=True
                print(i)
                break
        if isGood:
            break
else:
    for i in range(2,n):
        he=0
        temp=1
        while he<n:
            he+=temp
            temp*=i
            if he==n:
                isGood=True
                print(i)
                break
        if isGood:
            break