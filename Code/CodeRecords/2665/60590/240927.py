t=int(input())
for i in range(t):
    xyz=input()
    x=int(xyz.split(' ')[0])
    y=int(xyz.split(' ')[1])
    z=int(xyz.split(' ')[2])
    count=[0,0]
    while z!=1:
        if x%z==0:
            x-=1
            count[0]+=1
        elif y%z==0:
            y-=1
            count[1]+=1
        else:
            z-=1
    count = [str(x) for x in count]
    print(' '.join(count))