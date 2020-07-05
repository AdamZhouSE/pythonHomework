n=int(input())

for i in range(0,n):
    arr=input().split()
    if int(arr[1])*(int(arr[1])+1)/2 > int(arr[0]):
        print(0)
    else:
        print(1)
