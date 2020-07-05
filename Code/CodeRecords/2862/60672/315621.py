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
n=input()
arr=nums(input())
odd=[]
even=[]
for i in range(len(arr)):
    if arr[i]%2==0:
        even.append(arr[i])
    else:
        odd.append(arr[i])
total=abs(len(even)-len(odd))
answer=0
even=sorted(even,reverse=True)
odd=sorted(odd,reverse=True)
if total==0:
    print(answer)
else:
    m=min(len(even),len(odd))
    if len(even)==m:
        l=odd[m+1:]
        answer=sum(l)
    else:
        l=even[m+1:]
        answer=sum(l)
    print(answer)