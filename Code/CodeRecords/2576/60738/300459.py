arr=eval(input())
if arr//len(arr)<=min(arr):
    print(arr//len(arr))
else:
    for i in range(1,1000):
        for j in range(len(arr)):
            