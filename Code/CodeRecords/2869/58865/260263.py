n=int(input())
arr=input().strip().split(' ')
arr=[int(i) for i in arr]

newArr=[]
for i in reversed(range(len(arr))):
    if arr[i] not in newArr:
        newArr.append(arr[i])
        
newArr=[str(i) for i in newArr]
print(len(newArr))
print(' '.join(reversed(newArr)))