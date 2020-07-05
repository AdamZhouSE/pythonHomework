import sys
def count_num(array,i,T):
    result=[[1 for _ in range(2)] for _ in range(T-1)]
    for j in range(i):
        if (array[i][0]-array[j][0])==0:
            result[j][0]=sys.maxsize
        else:
            result[j][0]=(array[i][1]-array[j][1])/(array[i][0]-array[j][0])
    for j in range(i+1,T):
        if (array[i][0]-array[j][0])==0:
            result[j-1][0]=sys.maxsize
        else:
            result[j-1][0]=(array[j][1]-array[i][1])/(array[j][0]-array[i][0])
    result.sort()
    for j in range(T-2,0,-1):
        if result[j][0]==result[j-1][0]:
            result[j][1]=result[j][1]+result[j-1][1]
            result.pop(j-1)
    result.sort(key=lambda x:(-x[1]))
    return result[0][1]+1
T=int(input())
array=[[0 for _ in range(2)] for _ in range(T)]
for i in range(T):
    temp=input().split(',')
    array[i][0]=int(temp[0])
    array[i][1]=int(temp[1])
total=[]
for i in range(T):
    total.append(count_num(array,i,T))
print(max(total))