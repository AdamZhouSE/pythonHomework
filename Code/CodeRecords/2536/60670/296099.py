tickets=eval(input())
tickets=sorted(tickets,key=lambda x:(x[0],x[1]))
trip=[]
for i in range(0,len(tickets)):
    if tickets[i][0]=="JFK":
        trip.append(tickets[i][0])
        trip.append(tickets[i][1])
        del tickets[i]
        break
while tickets!=[]:
    back=trip[len(trip)-1]
    for i in range(0,len(tickets)):
        if tickets[i][0]==back:
            trip.append(tickets[i][1])
            del tickets[i]
            break
print(trip)