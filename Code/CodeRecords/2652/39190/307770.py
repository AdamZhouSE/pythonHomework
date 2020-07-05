def func2(arr,n,f):
    for i in range(len(arr)-int((n-1)/2)-1,-1,-1):
        ladd=0
        llist=[]
        radd=0
        rlist=[]
        for j in range(0,i):
            llist.append(arr[j][1])
        llist.sort()
        for k in range(int((n-1)/2)):
            ladd=ladd+int(llist[k])
        for l in range(i+1,len(arr)):
            rlist.append(arr[l][1])
        rlist.sort()
        for m in range(int((n-1)/2)):
            radd=radd+int(rlist[m])
        if ladd+radd+int(arr[i][1])<f:
            return arr[i][0]
    return -1
def takeFirst(elem):
    return int(elem[0])

ip1=input().split(" ")
arr=[]
for i in range(int(ip1[1])):
    arr.append(input().split(" "))
arr.sort(key=takeFirst)
op=int(func2(arr,int(ip1[0]),int(ip1[-1])))
print("%d "%(op))