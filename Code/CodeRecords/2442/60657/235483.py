lista=input()
lista=lista[1:-1]
lista=lista.split(',')
group = [int(n) for n in lista]
group.sort()
cons=[]
if len(group)==1:
    print("0")
else:   
    for i in range(0,len(group)-1):
        cons.append(group[i+1]-group[i])
    cons.sort()
    print(cons[-1])