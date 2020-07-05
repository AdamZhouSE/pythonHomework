flights=eval(input())
dict={}
for f in flights:
    if dict.get(f[0],0)!=0:
        dict[f[0]].append(f[1])
    else:dict[f[0]]=[f[1]]
res=[]
res.append('JFK')
for i in range(len(flights)):
    if dict.get(res[i],0)!=0:
        dict.get(res[i]).sort()
        res.append(dict.get(res[i])[0])
        dict[res[i]].pop(0)
    else:break
print(res)