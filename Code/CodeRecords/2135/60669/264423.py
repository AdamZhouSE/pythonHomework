arr=list(map(int,input().split(",")))
sum=0
for item in arr:
    sum+=item
average=sum/len(arr)


# if average!=int(average):
diff=sum
tempAverage=average
for item in arr:
    temp=abs(item-average)
    if temp<diff:
        diff=temp
        tempAverage=item
average=tempAverage


result=0
for item in arr:
    result+=abs(average-item)
print(result)