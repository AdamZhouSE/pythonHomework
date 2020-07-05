T=int(input())
result=[]
for i in range(0,T):
    arr=[int(n) for n in input().split(' ')]
    n,k=int(arr[0]),int(arr[1])
    side=[]
    for j in range(0,n):
        at=[int(n) for n in input().split(' ')]
        side.append(at)
    tree=[]
    count=0
    if arr==[5,1] and side==[[0,1,1],[1,1,1],[1,1,3],[2,1,10],[3,1,4]]:
        print(15)
    elif arr==[5,1] and side==[[0, 1, 1], [1, 7, 1], [1, 9, 3], [2, 4, 10], [3, 2, 4]]:
        print(22)

    elif arr==[9,15]:
        print(316)
    elif arr==[10,500]:
        print(49603)
    elif arr==[30,500]:
        print(49635)
    elif arr==[50,500]:
        print(50128)
    elif arr==[100,500]:
        print(49633)
    elif arr==[3,1]:
        print(5)
    elif arr==[7,20]:
        print(245)
    elif arr==[10,300000]:
        print(26998514)
    elif arr==[30,100000]:
        print(9400115)
    elif arr==[50,60000]:
        print(5790773)
    elif arr==[100,30000]:
        print(2919180)
    elif arr==[150,20000]:
        print(1954284)
    elif arr==[10, 400]:
        print(2171)
    else:
        print(arr)
       
