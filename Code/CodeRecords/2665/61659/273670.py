def shoot(shooter,saver):
    count=0
    while saver>1:
        if shooter%saver==0:
            shooter=shooter-1
            count=count+1
        else:
            saver=saver-1
    return count

T=int(input())

for k in range(0,T):
    temp=list(input().split(" "))
    shooter1=int(temp[0])
    shooter2=int(temp[1])
    saver=int(temp[2])

    print(str(shoot(shooter1,saver))+" "+str(shoot(shooter2,saver)))