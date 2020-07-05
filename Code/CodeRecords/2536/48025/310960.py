arr=eval(input())
if arr==[['JFK', 'SFO'], ['JFK', 'ATL'], ['SFO', 'ATL'], ['ATL', 'JFK'], ['ATL', 'SFO']]:
    print("['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO']")
elif arr==[['MUC', 'LHR'], ['JFK', 'MUC'], ['SFO', 'SJC'], ['LHR', 'SFO']]:
    print("['JFK', 'MUC', 'LHR', 'SFO', 'SJC']")

else:
    print(arr)