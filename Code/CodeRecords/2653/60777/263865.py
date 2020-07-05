t=int(input())

for i in range(t):
    temp=[int(x) for x in input().split()]
    res=(temp[0]-1)*10-(temp[0]-1)*temp[1]
    if(res>0):
        print(res)
    else:
        print(0)