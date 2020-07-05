arr=input().split(',')
for i in set(arr):
    if arr.count(i)>len(arr)//2:print(i)