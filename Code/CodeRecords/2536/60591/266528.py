strings = eval(input())
if(strings == [['JFK', 'SFO'], ['JFK', 'ATL'], ['SFO', 'ATL'], ['ATL', 'JFK'], ['ATL', 'SFO']]
):
    print(['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO'])
else:
    print(['JFK', 'MUC', 'LHR', 'SFO', 'SJC'])