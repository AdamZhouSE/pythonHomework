arr=eval(input())
target=int(input())
get=False
for i in range(len(arr)):
    if arr[i]==target:
        get=True
        print(i)
if not get:
    print(-1)