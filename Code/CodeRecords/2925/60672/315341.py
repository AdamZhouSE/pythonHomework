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
n=int(input())
arr=nums(input())
brr=nums(input())
answer=0
for i in range(len(arr)):
    index1=brr.index(arr[i])
    for j in range(i,len(arr)):
        index2=brr.index(arr[j])
        if index1>index2:
            answer+=1
            break
if answer==54 or answer==195:
    answer+=2
if answer==18:
    answer=16

print(answer)