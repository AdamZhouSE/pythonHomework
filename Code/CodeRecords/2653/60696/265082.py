n = int(input())
for i in range(n):
    arr = [int(j) for j in input().split()]
    print((arr[0]-1)*(10 - min(10, arr[1])))