num=int(input())
for k in range(num):
    n=int(input())
    l=n
    str=""
    time=1
    while(l>0):
        time=time*2
        if l%(time)<=time//2 and l%(time)!=0:
            str="4"+str
        else:
            str="7"+str
        l=l-time
    print(str)