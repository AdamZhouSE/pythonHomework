def count_num(array):
    value=[]
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j]==1:
                value.append([[i,j]])
    i=len(value)-1
    while i>-1:
        count=0
        union=[]
        for j in range(len(value[i])):
            m=value[i][j][0]
            n=value[i][j][1]
            if value.count([[m-1,n]])!=0:
                value[i].extend([[m-1,n]])
                union.append([[m-1,n]])
                count=count+1
            if value.count([[m+1,n]])!=0:
                value[i].extend([[m+1,n]])
                union.append([[m+1,n]])
                count=count+1
            if value.count([[m,n-1]])!=0:
                value[i].extend([[m,n-1]])
                union.append([[m,n-1]])
                count=count+1
            if value.count([[m,n+1]])!=0:
                value[i].extend([[m,n+1]])
                union.append([[m,n+1]])
                count=count+1
        if count>=1:
            for j in range(count):
                value.remove(union[j])
            i=i-count
        else:
            i=i-1
    return len(value)
num=input().split()
N=int(num[0])
M=int(num[1])
Q=int(num[2])
array=[[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    temp=input()
    for j in range(M):
        array[i][j]=int(temp[j])
for i in range(Q):
    temp=input().split()
    new_array=array[int(temp[0])-1:int(temp[2])]
    for j in range(len(new_array)):
        new_array[j]=new_array[j][int(temp[1])-1:int(temp[3])]
    print(count_num(new_array))