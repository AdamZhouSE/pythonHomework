T=int(input())
for i in range(0,T):
    arr=[int(n) for n in input().split(' ')]
    a,x,y,b,z=arr[0],arr[0],arr[1],arr[1],arr[2]
    while z!=1:
        if x%z==0:
            x-=1
        if y%z==0:
            y-=1
        else:
            z-=1
    print(a-x,b-y)