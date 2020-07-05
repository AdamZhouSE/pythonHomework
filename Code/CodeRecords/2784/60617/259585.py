def vote():
    init=input().split(" ")
    n=int(init[0])
    m=int(init[1])
    city=[]
    for i in range(0, m):
        city.append(list(map(int, input().split(" "))))
    winTimes=[0]*n
    for Acity in city:
        index=Acity.index(max(Acity))+1
        winTimes[index-1]+=1
    print(winTimes.index(max(winTimes))+1)


if __name__=='__main__':
    vote()