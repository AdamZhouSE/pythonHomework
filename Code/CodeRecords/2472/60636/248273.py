t=int(input())
for i in range(t):
    n=int(input())
    source=list(input())
    print(source)
    chongfus=[]
    for j in range(n):
        chongfu=False
        if(not source[j] in chongfus):
            for x in range(j+1,n):
                if(source[j]==source[x]):
                    chongfu=True
        else:
            chongfu=True
        if(not chongfu):
            print(source[j])
            break
        else:
            chongfus.append(source[j])
            