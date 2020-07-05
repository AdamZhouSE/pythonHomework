lista=input()
num=input()
tar=input()
num=int(num)
tar=int(tar)
lista=lista[1:-1]
lista=lista.split(',')
cons=[]
group = [int(n) for n in lista]
for x in group:
    cons.append(x-tar)
for x in range(0,len(cons)):
    if cons[x]<0:
       
        cons[x]=-cons[x]
dic=dict(zip(group,cons))
dic1=sorted(dic)
print(dic1[0:num])