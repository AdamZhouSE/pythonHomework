num=int(input())
l=list(map(int,input().split()))
numberOne=l.count(1)
numberTwo=l.count(2)
teamNumber=0
if numberOne>numberTwo:
    teamNumber=numberTwo+(numberOne-numberTwo)//3
else:
    teamNumber=numberOne
print(teamNumber)