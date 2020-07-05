count=int(input())
value=list(map(int,input().split()))   #5 4 3 2 1 1 1 1
doors=list(map(int,input().split()))   #2 3 1 1 2 7 6 8
start=1
while start<=count:   #start up
    step=[]
    total=value[start-1]
    step.append(start)
    nextdoor=doors[start-1]
    while nextdoor not in step:
        total=total+value[nextdoor-1]
        step.append(nextdoor)
        nextdoor=doors[nextdoor-1]
    print(total)
    start=start+1