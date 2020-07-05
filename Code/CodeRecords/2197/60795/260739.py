T=int(input())
for i in range(0,T):
    num=int(input())
    arr=[]
    for j in range(0,num):
        arr.append(j+1)
    index=0
    while len(arr)>1:
        killed=index+1
        if killed>len(arr)-1:
            killed=0
        del arr[killed]
        index=index+1
        if index>len(arr)-1:
            index=0
    print(arr[0])

