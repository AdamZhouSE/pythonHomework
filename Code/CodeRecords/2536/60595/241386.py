def Test():
    tickets=eval(input())
    flying=[]
    next=""
    for ticket in tickets:
        if(ticket[0]=="JFK"):
            flying.append("JFK")
            next=ticket[1]
            tickets.remove(ticket)
            break
    i=0
    while(tickets):
        if(tickets[i][0]==next):
            flying.append(next)
            next=tickets[i][1]
            if(len(tickets)==1):
                flying.append(next)
            tickets.remove(tickets[i])
            i=0
        else:
            i=i+1
    print(flying)
if __name__ == "__main__":
    Test()