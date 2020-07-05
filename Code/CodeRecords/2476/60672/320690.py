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
    n=input()
    arr=nums(input())
    arr=sorted(arr)
    summ=0
    for i in range(len(arr)):
        summ+=summ+arr[i]
    print(summ)