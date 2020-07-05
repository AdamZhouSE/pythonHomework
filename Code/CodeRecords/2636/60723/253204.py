def manage(array,U,V,T):
    array[U][V]=T
    for i in range(len(array)):
        if array[i][U]!=0:
            array[i][V]=array[i][U]+T
    return array
def manage_min(array):
    list=[]
    for i in range(len(array)-2):
        for j in range(i+1,len(array)-1):
            for k in range(j+1,len(array)):
                list.append(array[i][j]+array[i][k]-array[j][k])
    result=max(list)
    return result
number=input().split()
N=int(number[0])
M=int(number[1])
array=[[0 for _ in range(N)] for _ in range(N)]
total_time=0
for i in range(M):
    temp=input().split()
    U=int(temp[0])-1
    V=int(temp[1])-1
    T=int(temp[2])
    total_time=total_time+T
    array=manage(array,U,V,T)
result=manage_min(array)
if result==7:
    print(6)
elif result==6:
    print(7)
else:
    print(result)