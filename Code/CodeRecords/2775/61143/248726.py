T = eval(input())
num = []
B = ' '
s = 0
for i in range(T):
    num.append(eval(input()))
l = len(num)
for i in range(l):
    if num[i]%3 == 0:
        s = str(int(num[i]/3-1)) + B + str(int(num[i]/3)) + B + str(int(num[i]/3+1))
        print(s)
    else:
        print(-1)