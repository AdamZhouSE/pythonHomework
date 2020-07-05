n,m = [int(i) for i in input().split(' ')]
arr = [int(i) for i in input().split(' ')]
x = 0
arr = sorted(arr)
while x < m:
    x+=1
    i,j,k = [int(i) for i in input().split(' ')]
    print(arr[i+k-2])
    
    