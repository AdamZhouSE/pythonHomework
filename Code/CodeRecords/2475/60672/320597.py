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
t=int(input())
for i in range(t):
    arr=nums(input())
    length=1
    for i in range(len(arr)):
        value=arr[i]
        midlen=0
        for j in range(len(arr)):
            if value in arr:
                midlen+=1
                value+=1
        length=max(length,midlen)
    print(length)
    