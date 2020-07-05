size1 = list(map(int,input().split()))
choosen = list(map(int,input().split()))
lista = list(map(int,input().split()))
listb = list(map(int,input().split()))
lista.sort()
listb.sort()
a_max = lista[choosen[0]-1]
b_mix = listb[len(listb)-choosen[1]]
if a_max<b_mix:
    print("YES")
else:
    print("NO")