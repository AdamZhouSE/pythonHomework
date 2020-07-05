arr1=input()
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
cons=[]
for i in range(len(lista)):
    for k in range(lista[i][0],lista[i][1]+1):
        cons.append(k)
cons.sort()
final=[]
mid=[]
for i in range(len(cons)-1):
    if cons[i+1]-cons[i]>1:
        mid.append(i)
if(len(mid)==0):
    final.append([cons[0],cons[-1]])
else:
    final.append([cons[0],cons[mid[0]]])

    for i in range(len(mid)-1):
        start=mid[i]+1
        end=mid[i+1]
        temp=[]
        temp.append(cons[start])
        temp.append(cons[end])
        final.append(temp)
    final.append([cons[mid[len(mid)-1]+1],cons[-1]])
print(final)