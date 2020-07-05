import re
def longth(matrix):
    dir={}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            dir[(i,j)]=matrix[i][j]
    num_max=1
    dir_key=dir.keys()
    dvalue=[[1 for i in range(len(matrix[0]))]for j in range(len(matrix))]
    dir=sorted(dir.items(), key=lambda x:x[1])
    #print(dir)
    for dic in dir:
        i=dic[0][0]
        j=dic[0][1]
        if(i+1,j) in dir_key and matrix[i+1][j]<matrix[i][j] and dvalue[i][j]<dvalue[i+1][j]+1:
            dvalue[i][j] = dvalue[i + 1][j] + 1
        if (i - 1, j) in dir_key and matrix[i -1][j] < matrix[i][j] and dvalue[i][j] < dvalue[i - 1][j] + 1:
            dvalue[i][j] = dvalue[i - 1][j] + 1
        if (i , j-1) in dir_key and matrix[i ][j-1] < matrix[i][j] and dvalue[i][j] < dvalue[i ][j-1] + 1:
            dvalue[i][j] = dvalue[i ][j-1] + 1
        if (i , j+1) in dir_key and matrix[i ][j+1] < matrix[i][j] and dvalue[i][j] < dvalue[i ][j+1] + 1:
            dvalue[i][j] = dvalue[i ][j+1] + 1
        num_max=max(num_max,dvalue[i][j])
    return num_max
c=input()
n=''
for i in range(3):
    n=n+input()
list=re.split(r'[ \[ \] \n,]',(n[0:len(n)]))

list=[i for i in list if i !='']
#print(list)
arr=[]
for i in range(0,3):
        arr.append([])
        for j in range(0, 3):
            arr[i].append(list[i*3+j])
print(longth(arr))