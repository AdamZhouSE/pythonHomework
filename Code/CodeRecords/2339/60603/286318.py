testtime=int(input())
for i in range(testtime):
    num=int(input())
    list=input().split(" ")
    count=0
    for i in range(num):
        list[i]=int(list[i])
    stan = list.copy()
    stan.sort()
    for i in range(num):
        i=stan[i]
        loc=0
        stanloc=0
        for j in range(num):
            if(list[j]==i):
                loc=j
                break
        for j in range(num):
            if(stan[j]==i):
                stanloc=j
                break
        if(loc==stanloc):
            continue
        elif(loc>stanloc):
            
            for j in range(loc,stanloc,-1):
                mid=list[j]
                list[j]=list[j-1]
                list[j-1]=mid
                count+=1
        else:
            for j in range(loc,stanloc):
                mid=list[j]
                list[j]=list[j+1]
                list[j+1]=mid
                count+=1
    print(count)
    