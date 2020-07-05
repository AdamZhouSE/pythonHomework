n=int(input())
if n<=2:
    print(2)
elif n==3:
    print(3)
elif n<=5:
    print(5)
elif n<=7:
    print(7)
else:
    res=n
    while True:
        check=True
        for i in range(2,n):
            if res%i==0:
                check=False
                break
        if check:
            tem=str(res)
            h=True
            for i in range(int(len(tem)/2)):
                if tem[i]!=tem[len(tem)-i-1]:
                   h=False
                   break
            if h:
                break
        res+=1
    print(res)