arr=eval(input())
target=input()
isFound=False
for i in arr:
    if i>target:
        isFound=True
        break
if isFound:
    print(i)
else:
    print(arr[0])