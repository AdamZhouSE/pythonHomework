temp=[int(x) for x in input().split(',')]
tar=int(input())

res=[]
if tar in temp:
    res.append(temp.index(tar))
else:
    res.append(-1)
temp.reverse()
if tar in temp:
    res.append(len(temp)-1-temp.index(tar))
else:
    res.append(-1)
print(res)