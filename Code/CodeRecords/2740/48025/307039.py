arr=eval(input())

def getMin(t1,t2):
    arr1=t1.split(":")
    arr2=t2.split(":")
    arr1=list(map(int,arr1))
    arr2=list(map(int,arr2))
    if(arr1[0]==arr2[0]):
        return abs(arr1[1]-arr2[1])
    if(arr2[0]>arr1[0]):
        temp=arr2
        arr2=arr1
        arr1=temp
    # 此时 arr1 的 时针必定>arr2
    arr3=[]
    if(arr1[1]<arr2[1]):
        arr3.append(arr1[0]-arr2[0]-1)
        arr3.append(60-arr2[1]+arr1[1])
    else:
        arr3.append(arr1[0]-arr2[0])
        arr3.append(arr1[1]-arr2[1])
    #print(arr3)
    arr3_reverse=[24-arr3[0],0] if (arr3[1]==0) else [23-arr3[0],60-arr3[1]]
    #print(arr3_reverse)
    return arr3[0]*60+arr3[1] if(arr3[0]*60+arr3[1]<arr3_reverse[0]*60+arr3_reverse[1]) else arr3_reverse[0]*60+arr3_reverse[1]
min=getMin(arr[0],arr[1])
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        temp=getMin(arr[i],arr[j])
        if(temp<min):
            min=temp
print(min)
            