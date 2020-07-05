def addcandies(result,start,end,loads):
    temp=[]
    result[start]+=1
    if end in loads[start]:
        return result
    else:
        pre=start
        temp+=loads[start]
        while(temp):
            current=temp.pop(0)
            if(end in loads[current]):
                result[current]+=1
                return result
            else:
                temp2=loads[current][:]
                while(temp2):
                    nextnode=temp2.pop(0)
                    if(end in loads[nextnode]):
                        result[current]+=1
                        result[nextnode]+=1
                        return result; 
                    else:
                        nextnext=loads[nextnode]
                        for nn in nextnext:
                            if(end in loads[nn]):
                                result[current]+=1
                                result[nextnode]+=1
                                result[nn]+=1
                                return result
                

n=int(input())
loads=list(map(int,input().split(" ")))
edges=[[] for i in range(n)]
for i in range(n-1):
    x,y=map(int,input().split(" "))
    edges[x-1].append(y-1)
    edges[y-1].append(x-1)
result=[0 for i in range(n)]
for i in range(n-1):
    result=addcandies(result[:],loads[i]-1,loads[i+1]-1,edges[:])
    #print(result)
for i in result:
    print(i)
    