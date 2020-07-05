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
mat=lista.copy()
r, c = len(mat), len(mat[0])
for i in range(r):
    t, k = [], min(r - i, c)
    for j in range(k):
        t.append(mat[i + j][j])

    t.sort()
    for j in range(k):
        mat[i + j][j] = t[j]

for i in range(1, c):
    t, k = [], min(c - i, r)
    for j in range(k):
        t.append(mat[j][i + j])

    t.sort()
    for j in range(k):
        mat[j][i + j] = t[j]
print(mat)