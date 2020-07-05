arr=eval(input())
size=len(arr)
count=1
longest=1
for i in range(1,size):
    if arr[i]>arr[i-1]:
        count+=1
    else:
        count=1
    longest=max(longest,count)
print(longest)

