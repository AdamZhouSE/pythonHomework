def arr34():
    n=int(input())
    groups=[int(x) for x in input().split(' ')]
    c1,c2,c3,c4=0,0,0,0
    for num in groups:
        if(num==1):
            c1+=1
        elif(num==2):
            c2+=1
        elif(num==3):
            c3+=1
        elif(num==4):
            c4+=1
    res=0
    res+=c4+c3
    res+=c2//2
    remain=0
    if(c1>c3):
        remain=c1-c3
    if(c2%2!=0):
        res+=1
        remain=remain-2
    if(remain>0):
        res+=(remain//4)+1
    print(res)
    return

arr34()