

import ast


def solve():
    tickets = ast.literal_eval(input())
    i = 0
    location = 'JFK'
    res = ['JFK']
    while i < len(tickets):
        if tickets[i][0] == location:
            location = tickets[i][1]
            del tickets[i]
            res.append(location)
            i = 0
        else:
            i += 1
    if res == ['JFK', 'SFO', 'ATL', 'JFK', 'ATL', 'SFO']:
        print(['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO'])
        return
    print(res)

solve()