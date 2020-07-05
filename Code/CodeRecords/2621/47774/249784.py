arr_input=input().split(",")
arr=[]
for i in arr_input:
    arr.append(int(i))
max=arr[0]
sum=0
for i in arr:
    if sum>0:
        sum=sum+i
    if sum<=0:
        sum=i
    if sum>max:
        max=sum
print(max)