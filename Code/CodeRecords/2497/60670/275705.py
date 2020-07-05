target=int(input())
position=eval(input())
speed=eval(input())
n=len(speed)
car=[]
for i in range(0,n):
    car.append([position[i],speed[i]])
car=sorted(car,key=lambda x:-x[0])
print(car)