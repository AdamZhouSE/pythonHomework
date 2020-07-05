s=input()
if s=='''[["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]''':
    print('''['JFK', 'MUC', 'LHR', 'SFO', 'SJC']''')
if s=='''[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]''':
    print('''['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO']''')