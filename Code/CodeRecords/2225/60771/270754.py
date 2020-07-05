#18
from itertools import permutations
n = int(input())
m = int(input())
lights = []
choices = []
outcome = []
for i in range(0,n):
    lights.append(True) #用True和False来代表灯的亮暗情况
for i in range(0,m):
    for j in range(0,4):
        choices.append(j+1)
# print(lights)
# print(choices)
# print(",",choices[0])
choices = list(permutations(choices,m)) #从中选出m个步骤
# print(choices)
for steps in choices:
    # print("l",lights)
    temp = lights[:] #每次都从第一步开始，一次性完成
    # print("Again: ",temp)
    # print("s",steps)
    for s in steps:
        # print("in ",s)
        if s == 1:
            for i in range(0,len(temp)):
                temp[i] = not temp[i] #所有灯取反
                # print(temp[i])
        elif s == 2:
            for i in range(0,len(temp)):
                if (i+1) % 2 == 0:
                    temp[i] = not temp[i]
                    # print(temp[i])
        elif s == 3:
            for i in range(0,len(temp)):
                if (i+1) % 2 == 1:
                    temp[i] = not temp[i]
                    # print(temp[i])
        elif s == 4:
            for i in range(0,len(temp)):
                if (i+1) % 3 == 1:
                    temp[i] = not temp[i]
                    # print(temp[i])
    # print("temp: ",temp)
    if temp not in outcome:
        outcome.append(temp)
print(len(outcome))

