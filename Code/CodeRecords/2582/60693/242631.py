arr1=list(map(int,input().split(',')))
arr2=list(map(int,input().split(',')))
maxsum=0
for i in range(len(arr1)):
    for j in range(len(arr2)):
        sum=abs(arr1[i]-arr1[j])+abs(arr2[i]-arr2[j])+abs(i-j)
        if sum>maxsum:
            maxsum=sum
print(maxsum)