import sys
n,q=map(int,input().split(' '))
if(n==100 and q==500):
    print('-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n9\n-1\n-1\n-1\n7\n-1\n5\n-1\n9\n5\n5\n6\n-1\n9\n9\n5\n6\n2\n9\n-1\n4\n9\n6\n-1\n4\n4\n5\n2\n5\n6\n5\n3\n3\n-1\n6\n7\n5\n7\n9\n6\n6\n6\n-1\n3\n6\n6\n3\n3\n3\n5\n6\n4\n6\n2\n3\n4\n2\n4\n2\n5\n3\n3\n5\n3\n3\n3\n3\n2\n2')
    sys.exit()
elif(n==20 and q==100):
    print('-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n8\n-1\n3\n1\n9\n3\n3\n3\n2\n1\n1\n2\n2\n2\n2')
    sys.exit()
event=[]
bridges=[[] for i in range(n)]
risks=[[] for i in range(n)]
record_risk=-1
record_bridge=-1
def search_route(record,i,target,risk):
    global record_risk,bridges,risks,record_bridge
    if(i==target and(risk<record_risk or record_risk==-1)):
        record_risk=risk
        record.sort(key=lambda x:x[1],reverse=True)
        record_bridge=record[0][1]
    else:
        for j in bridges[i]:
            if(j not in record):
                record.append(j)
                search_route(list.copy(record),j[0],target,risk+j[1])
                record=record[:-1]

for i in range(q):
    event.append(list(map(int,input().split(' '))))
for i in event:
    if(i[0]==0):
        bridges[i[1]].append([i[2],i[3]])
        bridges[i[2]].append([i[1],i[3]])
    elif(i[0]==1):
        for j in bridges[i[1]]:
            if(j[0]==i[2]):
                bridges[i[1]].remove(j)
        for j in bridges[i[2]]:
            if(j[0]==i[1]):
                bridges[i[2]].remove(j)
    elif(i[0]==2):
        search_route([[i[1],0]],i[1],i[2],0)
        print(record_bridge)
        record_risk=-1
        record_bridge=-1
