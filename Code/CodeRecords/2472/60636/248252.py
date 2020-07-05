t=int(input())
for i in range(t):
    n=int(input())
    source=list(input())
    for j in range(n):
        chongfu=False
        for x in range(j+1,n):
            if(source[j]==source[x]):
                chongfu=True
        if(not chongfu):
            print(source[j])
            break