def orAndXor(arr):
    optimes=1
    array=arr
    while len(array)>1:
        tmp=[]
        if optimes%2:
            # doing or
            for i in range(0,len(array)-1,2):
                tmp.append(array[i]|array[i+1])
        else:
            # doing xor
            for i in range(0,len(array)-1,2):
                tmp.append(array[i]^array[i+1])
        array=tmp
        optimes+=1
    return array[0]

nm=input().split()
n,m=int(nm[0]),int(nm[1])
arr=list(map(int,input().split()))
for _ in range(m):
    pb=input().split()
    arr[int(pb[0])-1]=int(pb[1])
    print(orAndXor(arr))