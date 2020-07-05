def max(arr1,arr2):
    le = len(arr1)
    max = 0
    for i in range (0,le):
        for j in range(0,le):
            if abs(int(arr1[i])-int(arr1[j]))+abs(int(arr2[i])-int(arr2[j]))+abs(i-j)>max:
                max=abs(int(arr1[i])-int(arr1[j]))+abs(int(arr2[i])-int(arr2[j]))+abs(i-j)
    return max
arr1=input().split(",")
arr2=input().split(',')
print(max(arr1,arr2))