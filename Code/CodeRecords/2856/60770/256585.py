def solve():
    n=int(input())
    trees=[]
    for i in range(n):
        trees.append(list(map(int,input().split())))
    distance=[]
    for i in range(n-1):
        distance.append(trees[i+1][0]-trees[i][0])
    state=[0 for i in range(n)]
    state[0]=1
    state[n-1]=2

    for i in range(1,n-1):
        if distance[i-1]>trees[i][1]:
            state[i]=1
            continue
        else:
            if distance[i]>trees[i][1]:
                state[i]=2
                distance[i]-=trees[i][1]
            else:
                state[i]=0

    res=state.count(0)
    res=n-res
    print(res)

if  __name__ == '__main__' :
    solve()
