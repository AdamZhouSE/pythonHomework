n=int(input())
arr=[]
for i in range(0,n):
    arr=arr+[input().split()]
    for j in range(0,len(arr[i])):
        arr[i][j]=int(arr[i][j])
res=[arr[0]]
for k in range(0,n):
    res=[arr[0]]
    for i in range(1, len(arr)):
        p = True
        l = arr[i][0]
        r = arr[i][1]
        for j in range(0, len(res)):
            if l <= arr[j][1] and l >= arr[j][0]:
                if r >= arr[j][1]:
                    arr[j][1] = r
                    p = False
                    break
            if r >= arr[j][0] and r <= arr[j][1]:
                if l <= arr[j][0]:
                    arr[j][0] = l
                    p = False
                    break
        if p:
            res = res + [arr[i]]
    arr=res
for i in range(0,len(res)):
    for j in range(0,len(res)-1):
        if arr[j][0]>arr[j+1][0]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
for i in range(0,len(res)):
    print(str(arr[i][0])+' '+str(arr[i][1]))
