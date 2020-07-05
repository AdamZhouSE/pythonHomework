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
def difference(arr,k):
    answer=0
    if k>len(list(set(arr))):
        return -1
    m=0
    index=0
    for i in range(len(arr)):
        if arr.count(arr[i])>1:
            continue
        else:
            m=m+1
            if m==k:
                index=i
                break
    if m<k:
        return -1
    elif m==k:
        return arr[index]
t=int(input())
for i in range(t):
    nk=nums(input())
    n,k=nk[0],nk[1]
    arr=nums(input())
    answer=difference(arr,k)
    print(answer)