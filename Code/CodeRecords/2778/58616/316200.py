for _ in range(int(input())):
    s = input().split()
    a,b=int(s[0]),int(s[1])
    x=0
    for z in range(a,b+1):
        if z<10:
            x+=1
        else:
            s=str(z)
            if s[0]==s[-1]:
                x+=1
    print(x)