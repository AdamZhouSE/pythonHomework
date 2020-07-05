list0=input().split()
n=int(list0[0])
m=int(list0[1])
arr=[]
for i in range(n):
    lst=list(input())
    arr.append(lst)
count=0
for i in range(n):
    for j in range(m):
        if arr[i][j]=='2':
            arr[i][j]='*'
            count+=1
for i in range(n):
    for j in range(m-1):
        if arr[i][j]!='*' and arr[i][j+1]!='*':
            if int(arr[i][j])+int(arr[i][j+1])==4:
                arr[i][j]='*'
                arr[i][j+1]='*'
                count+=1
for i in range(n-1):
    for j in range(m):
        if arr[i][j]!='*' and arr[i+1][j]!='*':
            if int(arr[i][j])+int(arr[i+1][j])==4:
                arr[i][j]='*'
                arr[i+1][j]='*'
                count+=1
print(count)                