t=int(input())
for i in range(t):
    n=int(input())
    source=list(input())
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
            chongfus.append(source[j])
            