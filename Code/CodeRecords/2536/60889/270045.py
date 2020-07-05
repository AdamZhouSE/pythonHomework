def findWay(tickets,lastCity):
    if len(tickets)==0:
        return []
    choices = []
    for ticket in tickets:
        if ticket[0] == lastCity:
            choices.append(ticket)
    choices.sort()
    for choice in choices:
        newTickets = tickets.copy()
        newTickets.remove(choice)
        ways = findWay(newTickets,choice[1])
        ways.insert(0,choice)
        if len(ways) == len(tickets):
            return ways
    return []
            
    
    

rawTickets = input().replace(" ","")
rawTickets = rawTickets.strip("[\"]").split("\"],[\"")
tickets = []
for i in rawTickets:
    i = i.split("\",\"")
    tickets.append(i)
ways = findWay(tickets,"JFK")
route = ["JFK"]
for i in ways:
    route.append(i[1])
print(route)
