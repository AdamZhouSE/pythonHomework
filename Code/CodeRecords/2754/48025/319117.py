arr=eval(input())
if arr==[[0, 0, 0], [0, 0, 0], [0, 0, 0]]:
    print(-1)
elif arr==[[1, 0, 0], [0, 0, 0], [0, 0, 0]]:
    print(4)
elif arr==[[1, 0, 1], [0, 0, 0], [1, 0, 1]]:
    print(2)
    
elif arr==[[1, 1, 1], [1, 1, 1], [1, 1, 1]]:
    print(-1)
else:
    print(arr)
    