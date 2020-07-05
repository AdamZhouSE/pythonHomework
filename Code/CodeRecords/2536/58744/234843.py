tickets = dict(eval(input()))
sorted_tickets = list()
sorted_tickets.append('JFK')
cur_from = 'JFK'
while cur_from in tickets:
    sorted_tickets.append(tickets.get(cur_from))
    cur_from = tickets.get(cur_from)

print(sorted_tickets)
