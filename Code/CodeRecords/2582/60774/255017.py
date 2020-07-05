arr1 = list(map(int,input().split(',')))
arr2 = list(map(int,input().split(',')))
max = 0
for i in range(0,len(arr1) - 1):
    for j in range(i + 1,len(arr1)):
        if(abs(arr1[i] - arr1[j]) + abs(arr2[i] - arr2[j]) + j - i > max):
            max = abs(arr1[i] - arr1[j]) + abs(arr2[i] - arr2[j]) + j - i
print(max)