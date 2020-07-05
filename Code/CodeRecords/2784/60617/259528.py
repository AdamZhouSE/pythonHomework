def vote():
    init=input().split(" ")
    n=int(init[0])
    m=int(init[1])
    city=[]
    for i in range(0, m-1):
        city.append(list(map(int, input().split(" "))))
    poll=[]
    for i in range(0, n-1):
        count=0
        for j in range(0, m-1):
            count+=city[i][j]
        poll.append(count)
    print(poll.index(max(poll))+1)

if __name__=='__main__':
    vote()