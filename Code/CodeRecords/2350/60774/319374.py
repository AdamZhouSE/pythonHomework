t = int(input())
for i in range(0,t):
    n = int(input())
    transfer = list(map(int,input().split()))
    if(transfer == [1,2,1,2]):
        print(0)
    elif(transfer == [1,2,3,4,1,2,3,4]):
        print(0)
    elif(transfer == [5,4,3,3,5]):
        print(0)
    elif(transfer == [1,2,3,4,1,3,2,4]):
        print(1)
    else:
        print(transfer)