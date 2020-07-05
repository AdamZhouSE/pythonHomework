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
def midnum(arr):
    length = len(arr)
    if (length % 2)== 1:
        z=length // 2
        y = arr[z]
    else:
        y = int((arr[length//2]+arr[length//2-1])/2)
    return y
t=int(input())
for i in range(t):
    n=input()
    arr=nums(input())
    arr=sorted(arr)
    answer=midnum(arr)
    print(answer)