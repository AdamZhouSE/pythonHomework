number=input().split()
N=int(number[0])
M=int(number[1])
array=[]
cow=[[0 for _ in range(2)] for  _ in range(M)]
for i in range(N):
    array.append([int(input()),0])
for i in range(M):
    temp=input().split()
    cow[i][0]=int(temp[0])-1
    cow[i][1]=int(temp[1])-1
count=0
cow.sort()
for i in range(len(cow)-1,-1,-1):
    start=cow[i][0]
    end=cow[i][1]
    flag=True
    for j in range(start,end+1):
        if array[j][0]==array[j][1]:
            flag=False
    if flag:
        for j in range(start,end+1):
            array[j][1]=array[j][1]+1
        count=count+1
print(count)