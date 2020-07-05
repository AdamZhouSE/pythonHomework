t=eval(input())
for _ in range(t):
    arr=list(map(int,input().strip().split(' ')))
    print(arr[1]-arr[0]-1)