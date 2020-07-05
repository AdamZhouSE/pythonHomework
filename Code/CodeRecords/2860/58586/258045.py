nums=int(input())
arr=[]
for i in range(nums):
    arr.append(list(map(int,input().split(" "))))
x=[c[0] for c in arr]
max_x=max(x)
used_y=[]
used_x=[]
for c in arr:
    if c[0]==max_x:
        used_y.append(c[1])
count=0
for i in range(nums):
    if arr[i][0]==max_x or arr[i][1] in used_y or arr[i][0] in used_x:
        continue
    else:
        count+=1
        used_x.append(arr[i][0])
        used_y.append(arr[i][1])
print(count)