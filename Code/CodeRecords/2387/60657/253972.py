import re
A=input().split()
leng=int(A[0])
m=int(A[1])
arr=input().split()
arr=[int(x) for x in arr]
all=[]
for i in range(m):
    arr1=input().split()
    arr1 = [int(x) for x in arr1]
    all.append(arr1)
q=int(input())
def cal(A,all):
    for i in range(len(all)):
        temp=A[all[i][1]-1:all[i][2]]
        temp.sort()
        if all[i][0]==1:
            temp.reverse()
        A[all[i][1]-1:all[i][2]]=temp


    return A

print(cal(arr,all)[q-1])