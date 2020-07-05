
time=int(input())
result=[]
while time>0:
    pair=[]
    length=int(input())
    array=list(map(int,input().split()))
    dif=int(input())
    time=time-1
    i=0
    while i<length-1:
        j=i+1
        while j<length:
            if array[i]-array[j]==dif or array[j]-array[i]==dif:
                temp=[array[i],array[j]]
                temp.sort()
                pair.append(temp)
            j=j+1

        i=i+1
    countarray=[]
    for item in pair:
        if item not in countarray:
            countarray.append(item)

    result.append(len(countarray))
for res in result:
    print(res)

