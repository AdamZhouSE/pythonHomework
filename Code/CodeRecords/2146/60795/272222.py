T=int(input())
for i in range(0,T):
    arr=[int(n) for n in input().split(' ')]
    n,m,k=arr[0],arr[1],arr[2]
    store=[int(n) for n in input().split(' ')]
    result,road=[],[]
    for j in range(0,m):
        list=[int(n) for n in input().split(' ')]
        road.append(list)
    last=[int(n) for n in input().split(' ')]
    a,b=last[0],last[1]
    t,num,index,line=0,0,0,[]
    while index<len(road):
        if road[index][0]==a:
            num=num+1
            line.append(a)
            t=t+road[index][2]
            if road[index][1]==b:
                num=num+1
                line.append(b)
                break
            else:
                a=road[index][1]
        index=index+1
    ind,mark,humber,cola=0,0,0,0
    while ind<len(line):
        x=line[ind]
        if store[x-1]==1:
            cola=cola+1
        else:
            humber=humber+1
        if abs(humber-cola)>k:
            mark=1
            break
        ind=ind+1
    if abs(humber-cola)>k:
        mark=1
    if mark==1:
        print(-1)
    else:
        print(t)
            
            