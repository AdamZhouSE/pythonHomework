import re
def carFleet(target, position, speed):
    cars = [(pos, spe) for pos, spe in zip(position, speed)]
    sorted_cars = sorted(cars)
    times = [(target - pos) / spe for pos, spe in sorted_cars]
    stack = []
    for time in times[::-1]:
        if not stack:
            stack.append(time)
        else:
            if time > stack[-1]:
                stack.append(time)
    return len(stack)
target=int(input())
pos=re.findall("\d+",input())
speed=re.findall("\d+",input())
pos=[int(i) for i in pos]
speed=[int(i) for i in speed]
print(carFleet(target,pos,speed))