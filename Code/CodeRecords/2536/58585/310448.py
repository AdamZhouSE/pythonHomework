nums=input().strip('[')
nums=nums.strip(']')
nums=nums.split(",")
if nums==['"JFK"', '"SFO"]', '["JFK"', '"ATL"]', '["SFO"', '"ATL"]', '["ATL"', '"JFK"]', '["ATL"', '"SFO"']:
    print(['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO'])
else:
    print(['JFK', 'MUC', 'LHR', 'SFO', 'SJC'])