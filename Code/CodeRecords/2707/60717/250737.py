list1=eval(input())
lenn=len(list1)
count=0
for i in range(0,lenn,2):
    if list1[i]%2==0:
        lover=list1[i]+1
    else:
        lover=list1[i]-1
    for j in range(i+2,lenn):
        if list1[j]==lover:
            list1[i+1],list1[j]=list1[j],list1[i+1]
            count+=1
print(count)