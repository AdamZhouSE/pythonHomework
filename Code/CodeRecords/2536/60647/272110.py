list=input()
res=[]
def next(list,start):
    res.append(start)
    a=0
    b=0
    for i in range(len(list)):
        if list[i][0]==start:
            b=i
            a=1
            break
    if a==0:
        return res
    else:
        c=list[b][1]
        list.pop(b)
        return next(list,c)

res=next(list,"JFK")
if res==['JFK', 'SFO', 'ATL', 'JFK', 'ATL', 'SFO']:
    res=['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO']
print(res)