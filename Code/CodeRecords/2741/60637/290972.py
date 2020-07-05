arr=list(map(int,eval(input())))
record=1
start=0
for i in range(1,len(arr)):
    if(arr[i]<=arr[i-1]):
        if(i-start>record):
            record=i-start
        start=i
print(record)
