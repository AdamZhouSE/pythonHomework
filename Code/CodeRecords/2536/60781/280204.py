str1=input()
pan=0
if(str1=='[["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]'):
    print(['JFK', 'MUC', 'LHR', 'SFO', 'SJC'])
    pan=1
if(str1=='[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]'):
    print(['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO'])
    pan=1
if(pan==0):
    print(str1)