nums = eval(input())
dots = []
for i in range(0,nums):
    dot = list(map(int,input().split(',')))
    dots.append(dot)
dots.sort(key = (lambda x:x[1]))
tem = (dots[1][1]-dots[0][1])/(dots[1][0]-dots[0][0])
for i in range(0,nums-1):
    if tem != (dots[i+1][1]-dots[i][1])/(dots[i+1][0]-dots[i][0]):
        print("False")
        break
    if i == nums-2:
        print("True")
    