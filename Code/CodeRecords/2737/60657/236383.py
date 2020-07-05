num=input()
num=num[1:-1]
lista=num.split(',')
group = [int(n) for n in lista]
cons=[]
for x in group:
    if group.count(x)>len(group)//3:
        cons.append(x)

cons = list(set(cons))
print(cons)