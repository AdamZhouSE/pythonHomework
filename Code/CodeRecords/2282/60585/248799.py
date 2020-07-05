t=eval(input())
for _ in range(t):
    n=eval(input())
    arrival=list(map(int,input().strip().split()))
    departure=list(map(int,input().strip().split()))
    train=[]
    for i in range(n):
        train+=[[arrival[i],departure[i]]]
    train=sorted(train,key=lambda x:x[0])
    plantforms=[0]
    for i in range(len(train)):
        isEnough=False
        for j in range(len(plantforms)):
            if train[i][0]>plantforms[j]:
                plantforms[j]=train[i][1]
                isEnough=True
                break
        if not isEnough:
            plantforms.append(train[i][1])
    print(len(plantforms))