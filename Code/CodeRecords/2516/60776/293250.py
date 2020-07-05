a=int(input())
list=[]
for k in range(0,a):
    temp=input().split(',')
    for i in range(0,len(temp)):
        temp[i]=int(temp[i])
    list.append(temp)
max=0
for i in range(0,len(list)):
    if list[i][0]>max:
        max=list[i][0]
result=[]
for i in range(0,len(list)):
    temp=-1
    isright=0
    for j in range(list[i][1],max+1):
        for m in range(0,len(list)):
            if list[m][0] ==list[i][1]:
                temp=m
                isright=1
                break
        if isright==1:
            break
    result.append(temp)
print(result)