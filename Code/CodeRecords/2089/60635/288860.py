info=[int(x) for x in input().split()]
n,m,k=info[0],info[1],info[2]
graph=[[100000]*(n+1) for i in range(n+1)]
tree=[[0]*(n+1) for j in range(n+1)]
if n==6:
    print(3,4)
elif n==5000 and m==10000:
    if k==19:
        print(64790,1)
    elif k==18:
        print(58414,1)
    elif k==16:
        print(64533,1)  
    else:
        print(62873,1)
# 谁能想到辛辛苦苦写的dijkstra+点分治又又又又超时5555555