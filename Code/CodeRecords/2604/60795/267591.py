arr=eval(input())
target=input()
arr.sort()
index=-1
for i in range(0,len(arr)):
    if target<arr[i]:
        index=i
        break
if index==-1:
    index=0
print(arr[index])