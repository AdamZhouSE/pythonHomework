arr=eval(input())
num=[]
count=1
for i in range(len(arr)-1):
    count=1
    k=i
    for j in range(i+1,len(arr)):
        if arr[j]>arr[k]:
            count+=1
            k=j
        else:
            continue
    num.append(count)   
print(max(num))
