routes=eval(input())
list.sort(routes)
start="JFK"
result=['JFK']
while(len(routes)>0):
    for i in range(0,len(routes)):
        if(routes[i][0]==start):
            start=routes[i][1]
            result.append(start)
            del routes[i]
            break
print(result)


