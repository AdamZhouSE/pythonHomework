import math
num=int(input())
problems=[]
for i in range(num):
    problems.append(input())
for i in problems:
    temp=i.split()
    N=int(temp[0])
    L=int(temp[1])
    R=int(temp[2])
    key=0
    for i in range(L,R+1):
        key+=pow(2,i-1)
    print(N^key)