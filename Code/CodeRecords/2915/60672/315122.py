def nums(string):
    num='0123456789'
    nums=[]
    i=0
    while i<len(string):
        midstring=''
        k=0
        for j in range(i,len(string)):
            if string[j] in num:
                midstring+=string[j]
                k=k+1
            else:
                break
        if midstring!='':
            nums.append(int(midstring))
            midstring=''
            i=i+k
        else:
            i=i+1
            continue
    return nums

def find(arr):
    length=0
    for j in range(len(arr)-1):
        q=[arr[j],]
        k=0
        for i in range(j,len(arr)):
            if arr[i]/q[k]>1 and arr[i]/q[k]<2:
                q.append(arr[i])
                k=k+1
        length=max(length,len(q))

    return length

n=int(input())
arr=nums(input())
answer=find(arr)
print(answer)