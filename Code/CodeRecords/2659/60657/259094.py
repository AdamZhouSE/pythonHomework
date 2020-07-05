num=int(input())
for i in range(num):
    arr=input().split(' ')
    arr=[int(x) for x in arr]
    print(arr[1]-arr[0]-1)