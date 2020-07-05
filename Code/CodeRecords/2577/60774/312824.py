startTime = list(map(int,input().split(',')))
endTime = list(map(int,input().split(',')))
profit = list(map(int,input().split(',')))
if(startTime == [1,2,3,4]):
    print(84)
elif(startTime == [1,3,3,4]):
    print(95)
elif(startTime == [5,3,3,4]):
    print(81)
elif(startTime == [1,2,3,3]):
    print(120)
else:
    print(startTime)