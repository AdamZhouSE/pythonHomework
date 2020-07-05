def airline_plan():
    Tickets=eval(input())
    res=[]
    for ti in Tickets:
        temp=[]
        if ti[0]=="JFK":
            temp.append("JFK")
            temp.append(ti[1])
            tempList=list(Tickets)
            tempList.remove(ti)
            dfs(tempList,res,temp,ti)
    res.sort()
    for route in res:
        print(route)

def dfs(tickets, res, route,now):
    flag=0
    if not tickets:
        res.append(route)
        return
    for ti in tickets:
        if ti[0]==now[1]:
            temp=list(route)
            temp.append(ti[1])
            tempLi=list(tickets)
            tempLi.remove(ti)
            dfs(tempLi,res,temp,ti)
            flag=1
    if flag==0:
        res.append(route)

if __name__=='__main__':
    airline_plan()


