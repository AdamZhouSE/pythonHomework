import sys
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

l=int(input())
arr=[]
string=list(input())
arr=nums(string)
index=arr.index(max(arr))
indicate=0
for i in range(index):
    if arr[i]<arr[i+1]:
        continue
    else:
        indicate=1
        break
if indicate==1:
    print('NO')
else:
    c=0
    for i in range(index,len(arr)-1):
        if c==0:
            if arr[i+1]==max(arr):
                continue
            elif arr[i+1]<arr[i]:
                c=1
                continue
            else:
                indicate=1
                break
        else:
            if arr[i+1]<arr[i]:
                continue
            else:
                indicate=1
                break
    if indicate==1:
        print('NO')
    else:
        print('YES')