arr=[int(n) for n in input().split(' ')]
n,m,c=arr[0],arr[1],arr[2]
list=[int(n) for n in input().split(' ')]
re=[]
for i in range(0,n-m+1):
    mark=0
    max,min=list[i],list[i]
    for j in range(i+1,i+m):
        if list[j]>max:
            max=list[j]
        if list[j]<min:
            min=list[j]
    if max-min<=c:
        re.append(i+1)
if len(re)==0:
    print('NONE')
else:
    for i in range(0,len(re)):
        print(re[i])




