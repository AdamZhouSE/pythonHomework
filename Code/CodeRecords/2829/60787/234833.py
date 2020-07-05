n=int(input())
list=[int(i) for i in input().split()]
max,max2,min,min2=list[0],list[0],list[0],list[0]
for i in list:
    if i>max:
        max2=max
        max=i
    if i<=max and i>max2:
        max2=i
    if i<min:
        min2=min
        min=i
    if i>=min and i<min2:
        min2=i
print(min(max-min2,max2-min))