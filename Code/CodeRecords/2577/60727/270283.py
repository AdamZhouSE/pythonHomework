def so(start,end,p,pay):
    time = -1
    res=0
    for i in range(0,len(pay)):
        time = -1000
        temp=0
        for j in range(i,len(pay)):
            if start[j]>=time:
                if pay[j+1]>pay[j] and start[j]==start[j+1]:
                    temp+=j[+1]
                    i+=1
                    time = end[j+1]
                else:
                    temp+=pay[j]
                    time = end[j]
        if res<temp:
            res=temp
    return res         
start = list(map(int,input().split(',')))
end = list(map(int,input().split(',')))
pay = list(map(int,input().split(',')))
p=[]
for i in range(0,len(pay)):
    temp=[]
    temp.append(start[i])
    temp.append(end[i])
    p.append(temp)
print(so(start,end,p,pay))
               