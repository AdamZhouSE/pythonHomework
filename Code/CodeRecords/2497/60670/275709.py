target=int(input())
position=eval(input())
speed=eval(input())
n=len(speed)
car=[]
for i in range(0,n):
    car.append([position[i],speed[i]])
car=sorted(car,key=lambda x:-x[0])
num=n
for i in range(0,n-1):
    if (target-car[i][0])/car[i][1]>=(target-car[i+1][0])/car[i+1][1]:
        num-=1
print(num)