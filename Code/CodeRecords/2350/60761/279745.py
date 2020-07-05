def lesschange(n,changeStation):
    i=0
    while(i<len(changeStation)):
        if changeStation.count(changeStation[i])<2:
            changeStation.pop(i)
        elif(i<len(changeStation)-1 and changeStation[i]==changeStation[i+1]):
            changeStation.pop(i)
            changeStation.pop(i)
    


t=int(input())
for i in range(t):
    n=int(input())
    changeStation=list(map(int,input().split(" ")))
    print(lesschange(n,changeStation))