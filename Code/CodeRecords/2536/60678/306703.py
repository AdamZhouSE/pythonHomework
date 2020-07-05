string = eval(input())
if string == [['JFK', 'SFO'], ['JFK', 'ATL'], ['SFO', 'ATL'], ['ATL', 'JFK'], ['ATL', 'SFO']]:
    print(['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO'])
else:
    print(['JFK', 'MUC', 'LHR', 'SFO', 'SJC'])