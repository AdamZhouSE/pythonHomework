arr1=input().split(",")
arr2=input().split(",")
maxnum=0
for i in range(len(arr1)):
    for j in range(len(arr1)):
        maxnum=max(abs(int(arr1[i]) - int(arr1[j]))+abs(int(arr2[i]) - int(arr2[j]))+abs(i-j),maxnum)
print(maxnum)