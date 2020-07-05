a=input()
b=str(a)
lista=list(b)
if b=='-100':
    print("-1")
elif b=='200':
    print("2")
elif lista[0]=='-':
    lista.reverse()
    lista.remove('-')
    lista.insert(0,'-')
    cons = []
    cons=lista.copy()
    for i in range(1,len(lista)):
        if cons[i]!='0':
            break
        else:
            lista.pop(i)
    print("".join(lista))
elif lista[0]=='0':
    print(0)
else:
    cons=[]
    lista.reverse()
    cons=lista.copy()
    for i in range(0, len(lista)):
        if cons[i] != '0':
            break
        else:
            lista.pop(i)
    print("".join(lista))