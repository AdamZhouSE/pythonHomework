number = int(input())
str = input().split(' ')
lists = [int(i) for i in str]
sets = set(lists)
lista = list(sets)
if len(lista)<=2:
    if len(lista)==2:
        print(lista[1]-lista[0])
    else:
        print(lista[0])
else:
    lista.sort()
    alist = []
    for i in range(len(lista)):
        if i==len(lista)-1:
            break
        alist.append(lista[i+1]-lista[i])
    alist.sort()
    check=True
    for i in range(len(alist)):
        if alist[i]%alist[0]!=0:
            check=False
            break
    print(min(alist)) if check else print("-1")