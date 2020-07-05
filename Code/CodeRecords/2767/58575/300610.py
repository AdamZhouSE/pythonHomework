n=int(input())
for i in range(n):
    number=int(input())
    res=0
    j=0
    while j*10<=number:
        k=0
        while j*10+k*5<=number:
            if (number-j*10-k*5)%3==0:
                res=res+1
            k=k+1
        j=j+1
    print(res)