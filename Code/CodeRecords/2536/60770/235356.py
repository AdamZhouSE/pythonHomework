def solve():
    info=input()[2:-1].replace(' ','')+','
    tickets=list(map(lambda x:list(x.split(',')),map(lambda x:x.replace('"',''),map(lambda x:x[:-2],info.split('[')))))
    tickets.sort(key=lambda x:x[1])
    route=[]
    route.append('JFK')
    i=0
    for i in range(len(tickets)):
        route.append(find(route[i],tickets))
        i+=1
    print(route)

def find(leave,tickets=[]):
    for i in range(len(tickets)):
        if tickets[i][0]==leave:
            des=tickets[i][1]
            del tickets[i]
            return des

if  __name__ == '__main__' :
    solve()

