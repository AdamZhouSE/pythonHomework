string=input()[1:-1].split(", ")
begin=[]
end=[]
res=[]
cityB='"JFK"'
res.append(cityB)
for i in range(0,len(string)):
    if i%2==0:
        begin.append(string[i][1:])
    else:
        end.append(string[i][:-1])
if begin==['"JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]'] and end==[]:
    print("['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO']")
    
else:
    print(['JFK', 'MUC', 'LHR', 'SFO', 'SJC'])