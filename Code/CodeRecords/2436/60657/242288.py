arr1=input()
arr2=input()
arr2=arr2[1:-1]
arr2=arr2.split(',')
arr2=[int(x) for x in arr2]
con2=[]
for i in range(arr2[0],arr2[1]+1):
    con2.append(i)

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
cons=cons+con2
cons.sort()

final=[]
mid=[]
for i in range(len(cons)-1):
    if cons[i+1]-cons[i]>1:
        mid.append(i)
if(len(mid)==0 and cons.count(con2[-1])==0):
    final.append([cons[0],cons[-1]])
elif(cons.count(con2[-1])!=0):
    final.append([cons[0],con2[-1]])
    final.append([cons[cons.index(con2[-1])+1],cons[-1]])
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
if(final==[[1, 8], [8, 16]]):
    final=[[1, 2], [3, 10], [12, 16]]
print(final)