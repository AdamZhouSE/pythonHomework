t=eval(input())
for i in range(0,t):
    x=eval(input())
    arr=[]
    for j in range(0,x+1):
        if x&j==j:
            arr.append(j)
    for j in range(0,len(arr)):
        if j==len(arr)-1:
            print(arr[len(arr)-1-j],end=' ')
            print('')
        else:
            print(arr[len(arr)-1-j],end=' ')