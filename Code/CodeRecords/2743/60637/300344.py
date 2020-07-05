n=(int)(input())
routes=list(map(int,input().split(' ')))
relations=[]
neighbor=[[] for i in range(n)]
found_route=[]
def find_route(record,i,j):
    global neighbor,found_route
    if(i==j):
        found_route=record[:-1]
        return
    for k in neighbor[i-1]:
        judge = False
        if k not in record:
            judge=True
            record.append(k)
            find_route(list.copy(record),k,j)
            record=record[:-1]
for i in range(n-1):
    relations.append(list(map(int,input().split(' '))))
for i in relations:
    neighbor[i[0]-1].append(i[1])
    neighbor[i[1]-1].append(i[0])
candys=[0]*n
for i in range(n-1):
    find_route([routes[i]],routes[i],routes[i+1])
    for i in found_route:
        candys[i-1]+=1
for i in candys:
    print(i)
