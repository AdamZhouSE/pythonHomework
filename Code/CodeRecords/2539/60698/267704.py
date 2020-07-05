#35
arr=list(eval(input()))
sorted_arr=sorted(arr)
begin=-1
end=-1
for i in range(0,len(arr)):
    if arr[i]!=sorted_arr[i]:
        begin=i
        break
for i in range(len(arr)-1, -1,-1):
    if arr[i] != sorted_arr[i]:
        end = i
        break
if begin==-1 or end==-1:
    print(0)
else:
    print(end-begin+1)
