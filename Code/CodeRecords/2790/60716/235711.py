n,m = map(int,input().split())
stra = input().split(' ')
strb = input().split(' ')
lista = [int(i) for i in stra]
listb = [int(i) for i in strb]
lista.sort()
lists = []
for i  in range(m):
    index = listb[i]
    if min(lista)>index:
        lists.append(0)
    else:
        for j in range(n):
            if lista[n-1-j]<=index:
                lists.append(n-j)
                break
for k in range(m-1):
    print(lists[k],end=' ')
print(lists[m-1])