airlines=input().replace(" ","")
airlines=list(map(str,airlines[2:-2].split("],[")))
result=[]
result.append("JFK")
i=0
while(0<len(airlines)):
    destination=[]
    for airline in airlines:
        if(airline.startswith('"'+result[i])):
            destination.append(airline[7:-1])
    destination.sort()
    airlines.remove('"'+result[i]+'","'+destination[0]+'"')
    result.append(destination[0])
    i=i+1
print(result)
