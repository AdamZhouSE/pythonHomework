num=input()
num=num[1:-1]
lista=num.split(',')
group = [int(n) for n in lista]
cons=[]
jud=1
for i in range(0,len(group)-1):
    cons.append(jud)
    if(group[i+1]<=group[i]):
        cons.append(jud)
        jud=1
    else:
        jud+=1
cons.sort()
cons.reverse()
print(cons[0])