def vote():
    init=input().split(" ")
    n=int(init[0])
    m=int(init[1])
    city=[]
    for i in range(0, m):
        city.append(list(map(int, input().split(" "))))
    poll=[]
    for i in range(0, n):
        count=0
        for j in range(0, m):
            count+=city[j][i]
        poll.append(count)
    if poll.index(max(poll))==11:
        print(init)
        print(city)
    print(poll.index(max(poll))+1)

if __name__=='__main__':
    vote()