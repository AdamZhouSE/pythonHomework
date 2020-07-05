t=int(input())
for i in range(t):
    x=int(input())
    y=1
    loc=-1
    for i in range(1,33):
        if(x&y):
            if(loc!=-1):
                loc=-1
                break
            loc=i
        y<<=1
    print(loc)