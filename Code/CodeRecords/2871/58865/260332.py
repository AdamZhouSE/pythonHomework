n=int(input())
arr=input().strip().split(' ')
arr=[int(i) for i in arr]

arr.sort()
index=len(arr)
for i in arr:
    if i==2:
        index=arr.index(i)
one=arr[:index]
two=arr[index:]
gap=len(one)-len(two)
count=min(len(one),len(two))+(gap//3 if gap>0 else 0)
print(count)
