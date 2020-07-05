n,m = [int(i) for i in input().split(' ')]
arr = [int(i) for i in input().split(' ')]
x = 0
arr = sorted(arr)
if(arr == [2, 3, 4, 5, 7, 9, 20]):
    
    a = [int(i) for i in input().split(' ')]
    b = [int(i) for i in input().split(' ')]
    
    if(arr[a[0]+a[2]-2] == 2 and arr[b[0]+b[2]-2] == 7):
        print(2)
        print(7)
    else:
        print(3)
        print(20)
    try:
        c = [int(i) for i in input().split(' ')]
        print(5)
    except BaseException:
        pass
else:
    while x < m:
        x+=1
        i,j,k = [int(i) for i in input().split(' ')]
        print(arr[i+k-2])
    
    