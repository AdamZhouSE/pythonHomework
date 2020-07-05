def josephus(n):
    lista=[]
    for i in range(n):
        lista.append(i+1)
    index = 0
    while len(lista)>1:
        temp = lista.pop(0)
        index += 1
        if index == 2:
            index = 0
            continue
        lista.append(temp)
    print(lista[0])
num=int(input())
for i in range(num):
    n=int(input())
    josephus(n)
