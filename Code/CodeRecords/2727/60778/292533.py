UCs=int(input())
for UC in range(UCs):
    rb=input()
    mice=list(map(int,input().split()))
    holes=list(map(int,input().split()))
    mice.sort()
    holes.sort()
    distance=[]
    for i in range(len(mice)):
        distance.append(abs(mice[i]-holes[i]))
    print(max(distance))