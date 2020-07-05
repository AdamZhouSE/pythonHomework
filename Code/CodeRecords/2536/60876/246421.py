ticket=eval(input())
ticket.sort()
start=[]
des=[]
result=["JFK"]
current="JFK"
for item in ticket:
    start.append(item[0])
    des.append(item[1])
while current in start:
    index=start.index(current)
    current=des[index]
    start[index]="#"
    des[index]="#"
    result.append(current)
print(result)