str0=input()
list0=str0.split()
lin=int(list0[0])
col=int(list0[1])
linl=[0]*col
matrix=[]
for i in range(lin):
    matrix.append(linl)

for i in range(lin):
    st=input()
    for j in range(col):
        matrix[i][j]=st[j]



