def minvalue(weight,Day):
    maximum = 0
    res = 0
    for x in range(0, len(weight)):
        if weight[x] > maximum:
            maximum = weight[x]
        res += weight[x]
    Capitivity = max(res // Day, maximum)
    while True:
        sum=0
        day=1
        for t in range(0, len(weight)):
            if weight[t]+sum<=Capitivity:
                sum+=weight[t]
            else:
                sum=weight[t]
                day+=1
        if day<=Day:
            return Capitivity
        else:
            Capitivity+=1
a=input()
a=a[1:len(a)-1]
store=[]
store.append(list(map(int, a.split(","))))
weight=store[0]
Day=int(input())
print(minvalue(weight,Day))