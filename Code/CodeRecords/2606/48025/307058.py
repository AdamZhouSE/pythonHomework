arr=eval(input())
target=int(input())
if target in arr:
    print(arr.index(target))
    
else:
    print(-1)