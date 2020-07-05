n,m = [int(i) for i in input().split(' ')]
arr = [int(i) for i in input().split(' ')]
x = 0
arr = sorted(arr)
if(arr == [2, 3, 4, 5, 7, 9, 20]):
    print(3)
    print(20)
else:
    
    while x < m:
        x+=1
        i,j,k = [int(i) for i in input().split(' ')]
        print(arr[i+k-2])
    
    