lines=input()
lines=lines.replace("[","").replace("]","")
arr=list(map(int,lines.split(",")))
count=0
i=0
min=10
max=-1
start=0
for i in range(len(arr)):
    if arr[i]<min:
        min=arr[i]
    if arr[i]>max:
        max=arr[i]
    if max==i and min==start:
        count+=1
        start=i+1
        min=10
        max=-1
    i+=1
print(count)