T=int(input())
for i in range(0,T):
    arr=[int(n) for n in input().split(' ')]
    node,side=arr[0],arr[1]
    sideset=[]
    for j in range(0,side):
        list=[int(n) for n in input().split(' ')]
        sideset.append(list)
    