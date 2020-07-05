time=int(input())
while(time>0):
    time-=1
    num=int(input())
    list0=[]
    for i in range(1,num+1):
        list0.append(str(bin(i))[2:])
    print(*list0,end='')
    print(" ")