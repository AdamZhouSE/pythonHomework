n=int(input())
for i in range(n):
    number=int(input())
    if number%2==1:
        count=0
        res=2
        while count<number//2:
            res=res**2
            count+=1
    else:
        count=0
        res=2
        while count<(number-1)//2:
            res=res**3
            count+=1
    print(res)