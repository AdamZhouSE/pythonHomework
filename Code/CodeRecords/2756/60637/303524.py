n=(int)(input())
red_edges=eval(input())
blue_edges=eval(input())
red_relations=[[] for i in range (n)]
blue_relations=[[] for i in range (n)]
for i in red_edges:
    red_relations[i[0]].append(i[1])
for i in blue_edges:
    blue_relations[i[0]].append(i[1])
record_route=-1
def dfs(record,i,target,color):
    global  red_relations,blue_relations,record_route
    if(i==target and len(record)>record_route):
        record_route=len(record)-1
        return
    if(color=='red'):
        for j in red_relations[i]:
            if(j not in record):
                record.append(j)
                dfs(list.copy(record),j,target,'blue')
                record=record[:-1]
    else:
        for j in blue_relations[i]:
            if (j not in record):
                record.append(j)
                dfs(list.copy(record), j, target, 'red')
                record=record[:-1]
result=[]
for i in range(n):
    dfs([0],0,i,'red')
    result.append(record_route)
    record_route=-1
print(result)