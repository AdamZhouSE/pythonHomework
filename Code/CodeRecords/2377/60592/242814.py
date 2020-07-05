num = input()
dots = []
for i in range(0,3):
    ls = list(map(int,input().split(',')))
    dots.append(ls)
dots.sort(key = (lambda x:x[0]))
tem = (dots[1][1]-dots[0][1])/(dots[1][0]-dots[0][0])
if tem != (dots[2][1]-dots[1][1])/(dots[2][0]-dots[1][0]):
    print("True")
else:
    print("False")