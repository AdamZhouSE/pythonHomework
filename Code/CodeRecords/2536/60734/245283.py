import re
lst = re.findall(r'\w+',input())

info = []
for i in range(0,len(lst),2):
    info.append([lst[i],lst[i+1]])
info = sorted(info, key=lambda x: x[1])
froms = []
for i in range(len(info)):
    froms.append(info[i][0])
    
route = ['JFK']
count = 0
while len(froms) != 0:
    index = froms.index(route[count])
    route.append(info[index][1])
    del froms[index]
    del info[index]
    count+=1
print(route)