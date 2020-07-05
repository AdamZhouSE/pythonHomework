num=input().strip().split(' ')
num=[int(i) for i in num]
arr=input().strip().split(' ')
arr=[int(i) for i in arr]
i=0
options=[]
low=high=0
temp1=temp2=[]
for i in range(0,num[1]):
    temp=input().strip().split(' ')
    temp=[int(i) for i in temp]
    options.append(temp)
q=int(input().strip())
for i in range(0,num[1]):
    low=options[i][1]-1
    high=options[i][2]
    if options[i][0]==0:
        temp1=sorted(arr[low:high])
        temp2=arr[high:]
        arr=arr[:low]
        temp1.extend(temp2)
        arr.extend(temp1)
    else:
        temp1=sorted(arr[low:high],reverse=True)
        temp2=arr[high:]
        arr=arr[:low]
        temp1.extend(temp2)
        arr.extend(temp1)
print(arr[q-1])
