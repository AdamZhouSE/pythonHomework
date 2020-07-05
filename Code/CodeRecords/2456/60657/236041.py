lista=input()
lista=lista[1:-1]
lista=lista.split(',')
group = [int(n) for n in lista]
cons=[]
con=0
for i in range(0,len(group)):
    for k in range(i+1,len(group)):
        if(group[k]<group[i]):
            con+=1
    cons.append(con)
    con=0
print(cons)