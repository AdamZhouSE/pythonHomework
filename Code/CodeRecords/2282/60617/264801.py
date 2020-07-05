def train():
    T=int(input())
    for i in range(0,T):
        calPlatform()

def calPlatform():
    N=int(input())
    arrival=input().split(" ")
    leave=input().split(" ")
    arrival=list(map(transformTime(), arrival))
    leave=list(map(transformTime(), leave))
    minPlatform=1
    for i in range(0, N):
        temp=1
        for j in range(arrival[i], minPlatform[i]):
            if j in arrival:
                temp+=1
        minPlatform=max(minPlatform, temp)
    print(minPlatform)

def transformTime(Hmmm):
    minute=0
    minute+=int(Hmmm)[0]*600
    minute+=int(Hmmm)[1]*60
    minute+=int(Hmmm)[2]*10
    minute++int(Hmmm)[3]*1
    return minute