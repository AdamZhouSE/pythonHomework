str1 = input().split(',')
str2 = input().split(',')
lista = [int(i) for i in str1]
listb = [int(i) for i in str2]
lista.extend(listb)
lista.sort()
if len(lista)%2==1:
    print(lista[(len(lista)-1)//2])
else:
    print('{:.5f}'.format((lista[(len(lista)-1)//2] + lista[(len(lista)+1)//2])/2))