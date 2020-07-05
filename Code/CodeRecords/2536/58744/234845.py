tickets = dict(eval(input()))
sorted_tickets = list()
sorted_tickets.append('JFK')
cur_from = 'JFK'
while cur_from in tickets:
    cur_to = tickets.get(cur_from)
    sorted_tickets.append(cur_to)
    tickets.pop(cur_from)
    cur_from = cur_to

print(sorted_tickets)
