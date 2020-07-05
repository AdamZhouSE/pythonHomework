arr=input().replace("[","").replace("]","").split(",")
carr=arr.copy()
arr.sort()
start=0
count=0
for i in range(len(arr)):
    end=i+1
    new=carr[start:end]
    new.sort()
    if(new==arr[start:end]):
        count=count+1
        start=i+1
print(count)