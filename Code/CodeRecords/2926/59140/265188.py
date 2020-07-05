n=int(input())
arr=input().split(" ")
max=0
for i in arr:
    if arr.count(i)>max:max=arr.count(i)
print(max)