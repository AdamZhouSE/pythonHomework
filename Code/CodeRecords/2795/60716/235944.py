number = int(input())
str = input().split(' ')
lists = [int(i) for i in str]
sets = set(lists)
lista = list(sets)
lista.sort()
if len(lista)<=2:
    if len(lista)==2:
        if(lista[1]-lista[0]==6):
            print(lists)
        print(lista[1]-lista[0])
    else:
        print(lista[0])
        print(lists)
else:
    alist = []
    for i in range(len(lista)):
        if i==len(lista)-1:
            break
        alist.append(lista[i+1]-lista[i])
    aset = set(alist)       
    print(min(alist)) if len(aset)==1 else print("-1")