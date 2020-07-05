n=eval(input())
m=[]
arr=[]
temp=[]
total=1
for i in range(0,n):
    m.append(eval(input()))
    temp=input().strip().split(' ')
    temp=[int(j) for j in temp]
    arr.append(temp)
for i in range(0,n):
    total=1
    for j in arr[i]:
        total*=j
    for j in arr[i]:
        print(total//j,end=' ')
    print()