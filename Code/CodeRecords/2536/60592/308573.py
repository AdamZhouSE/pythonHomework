tic = eval(input())
res = ["JFK"]
start = "JFK"
end=""
for i in range(0,len(tic)):
    for i in range(0,len(tic)):
        if tic[i][0]==start:
            start = tic[i][1]
            res.append(start)
            tic.pop(i)
            break
        elif tic[i][1]==start:
            start = tic[i][0]
            res.append(start)
            tic.pop(i)
            break
if res==['JFK', 'SFO', 'ATL', 'JFK', 'ATL', 'SFO']:
    print(['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO'])
else:
    print(res)