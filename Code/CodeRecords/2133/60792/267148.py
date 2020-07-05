list1=list(map(int,input().split(",")))
sum=0
min=list1[0]
for i in range(0,len(list1)):
    sum=sum+list1[i]
    if list1[i]<min:
        min=list1[i]
print(sum-min*len(list1))