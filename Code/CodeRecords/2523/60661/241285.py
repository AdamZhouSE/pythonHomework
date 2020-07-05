mat=input()[2:-2].split('],[')
for i in range(len(mat)):
    mat[i]=str(mat[i]).split(',')
    mat[i]=[int(x) for x in mat[i]]
for j in range(len(mat[0])-1):
    a=j;b=0
    temp=[]
    while a<len(mat[0]) and b<len(mat):
        temp.append(mat[b][a])
        a+=1;b+=1
    temp.sort()
    a=j;b=0;k=0
    while a < len(mat[0]) and b < len(mat):
        mat[b][a]=temp[k]
        a += 1;b += 1;k+=1
for j in range(1,len(mat)-1):
    a=0;b=j
    temp=[]
    while a<len(mat[0]) and b<len(mat):
        temp.append(mat[b][a])
        a+=1;b+=1
    temp.sort()
    a=0;b=j;k=0
    while a < len(mat[0]) and b < len(mat):
        mat[b][a]=temp[k]
        a += 1;b += 1;k+=1
print(mat)
