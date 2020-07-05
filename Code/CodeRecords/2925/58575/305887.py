n=int(input())
enter=list(map(int,input().split(" ")))
exitCar=list(map(int,input().split(" ")))

carIn=[[0] for i in range(n)]
carOut=[[0] for i in range(n)]

for i in enter:
    carIn[i-1]=enter[0:enter.index(i)]
for i in exitCar:
    carOut[i-1]=exitCar[0:exitCar.index(i)]

number=0
i=0
while i<n:
    for j in carIn[i]:
        if j not in carOut[i]:
            number+=1
            break
    i+=1

print(number)