arr=[int(n) for n in input().split(',')]
target=int(input())
start,end=-1,-1
for i in range(0,len(arr)):
    if arr[i]==target:
        if start==-1:
            start,end=i,i
        else:
            if i>end:
                end=i
list=[start,end]
print(list)