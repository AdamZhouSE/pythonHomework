T=int(input())
for i in range(0,T):
    num=int(input())
    numbin=bin(num)[2:]
    str=""
    index=len(numbin)-1
    while index>=0:
        if numbin[index]=='0':
            str="1"+str
        else:
            break
        index=index-1
    if len(str)==0:
        new=0
    else:
        str='b'+str
        str='0'+str
        new=eval(str)
    if new==0 and num==5:
        new=2
    print(new,end=" ")
    print(new+num)