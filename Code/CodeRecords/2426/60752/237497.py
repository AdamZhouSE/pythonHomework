testnum=int(input())
for i in range(0,testnum):
    num=int(input())
    abl=list(map(int,input().split(' ')))
    max=0
    for a in range(0,num-2):
        abl1=abl[a]
        for b in range(a+1,num-1):
            abl2=abl[b]
            for c in range(b+1,num):
                abl3=abl[c]
                if abl1*abl2*abl3>max:
                    max=abl1*abl2*abl3
    print(max)