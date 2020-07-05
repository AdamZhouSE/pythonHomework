t=int(input())
for i in range(t):
    n=int(input())
    source=list(input())
    alls=[]
    for i in source:
        if(not i in alls):
            alls.append(i)
    chongfus=[]
    for j in range(len(source)):
        chongfu=False
        if(source[j] in chongfus):
            chongfu=True
        else:
            for x in range(j+1,n):
                if(source[j]==source[x]):
                    chongfu=True
        if(not chongfu):
            print(source[j])
            break
        else:
            if(not source[j] in chongfus):
                chongfus.append(source[j])
    if(len(chongfus)==len(alls)):
        print(-1)