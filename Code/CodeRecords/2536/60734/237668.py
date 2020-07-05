import re
string = input()
lst = re.findall(r'\w+',string)

froms = []
tos = []
for i in range(len(lst)):
    if i%2==0:
        froms.append(lst[i])
    else:
        tos.append(lst[i])

route = ['JFK']
count = 0
index = 0
while len(tos) != 0:
    index = froms.index(route[count])
    route.append(tos[index])
    del froms[index]
    del tos[index]
    count+=1
print(route)