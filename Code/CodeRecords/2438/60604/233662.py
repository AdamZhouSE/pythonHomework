list=input().lstrip('[').rstrip(']').split(',')
size=len(list)
for i in range(size):
    list[i]=int(list[i])
for i in range(size):
    for j in range(size-1,i,-1):
        if list[j]<=list[j-1]:
            temp=list[j]
            list[j]=list[j-1]
            list[j-1]=temp
print(list)
        