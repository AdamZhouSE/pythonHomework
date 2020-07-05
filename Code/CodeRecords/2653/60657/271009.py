n=int(input())
for i in range(n):
    arr=input().split(' ')
    arr=[int(x) for x in arr]
    print((arr[0]-1)*(10-arr[1]))