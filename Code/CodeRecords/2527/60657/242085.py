arr1=input()
veg=input()
veg=int(veg)
pri=input()
pri=int(pri)
dis=input()
dis=int(dis)
arr1=arr1[1:-1]
lista=[]
start=0
end=0
for i in range(len(arr1)):
    if(arr1[i]=='['):
        str1=''
        for k in range(i+1,len(arr1)):
            if(arr1[k]==']'):
                start=i
                end=k
                break
        for m in range(start,end):
            str1+=arr1[m]
        lista.append(str1)
for i in range(len(lista)):
    lista[i]=lista[i][1:]
    lista[i]=lista[i].split(',')
    lista[i]=[int(x) for x in lista[i]]
hot=[]
for i in range(len(lista)):
    if(veg==1):
        if(lista[i][2]!=veg):
            hot.append(i)
        if (lista[i][3] > pri):
            hot.append(i)
        if (lista[i][4] > dis):
            hot.append(i)
    else:
        if(lista[i][3]>pri):
            hot.append(i)
        if(lista[i][4]>dis):
            hot.append(i)
set(hot)
temp=[]
for i in hot:
    temp.append(lista[i])
cons=[x for x in lista if x not in temp]
rate=[]
for i in range(len(cons)):
    rate.append((cons[i][1],cons[i][0]))
rate.sort()
rate.reverse()
final=[]
for i in range(len(rate)):
    final.append(rate[i][1])
print(final)
