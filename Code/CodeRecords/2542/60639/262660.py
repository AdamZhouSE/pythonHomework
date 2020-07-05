arr=eval(input())
arr.sort()
num=[]
count=1
for i in range(len(arr)-1):
    if arr[i+1]==arr[i]+1:
        count+=1
    else:
        num.append(count)
        count=1
print(max(num))