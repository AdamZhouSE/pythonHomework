n=(int)(input())
edges=eval(input())
src=(int)(input())
dst=(int)(input())
k=(int)(input())
aline=[]
def flight(cost,record,src,dst,stations):
    global edges,aline
    if(stations>k+1):
        return
    if(src==dst):
        aline.append(cost)
        return
    for i in edges:
        if(i[0]==src and[i[0],i[1]] not in record):
            record.append([i[0],i[1]])
            flight(cost+i[2],list.copy(record),i[1],dst,stations+1)
            record=record[:-1]
flight(0,[],src,dst,0)
print(min(aline))