arr=raw_input().split(',')
le=len(arr)
for i in range(0,le):
    arr[i]=int(arr[i])
re=0
new=-4
for j in range(0,le):
    for k in range(j+1,le):
        if arr[k]==arr[j]:
           re=arr[j]
for l in range(1,le+1):
    op=0
    for m in range(0,le):
        if arr[m]==l:
            op=1
    if op==0:
        new=l
        break
list=[re,new]
print(list)