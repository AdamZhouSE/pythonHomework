init=eval(input())
init.sort()
key="JFK"
route=["JFK"]
while len(init)>0:
    for i in range(len(init)):
        if init[i][0]==key:
            route.append(init[i][1])
            key=init[i][1]
            del init[i]
            break
print(route)