a=input()
b=str(a)
lista=list(b)
if lista[0]=='-':
    lista.reverse()
    lista.remove('-')
    lista.insert(0,'-')
    for i in range(1,len(lista)):
        if lista[i]!='0':
            break
        else:
            lista.pop(i)
    print("".join(lista))
else:
    lista.reverse()
    for i in range(0, len(lista)):
        if lista[i] != '0':
            break
        else:
            lista.pop(i)
    print("".join(lista))