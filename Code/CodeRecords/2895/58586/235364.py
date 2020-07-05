lines=input().replace("[","").replace("]","")
arr=list(map(int,lines.split(",")))
left=arr[0]
right=arr[1]
result=left
for i in range(left+1,right+1):
    result&=i
    i+=1
print(result)