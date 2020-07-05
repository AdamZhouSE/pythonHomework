# 6
inp = input()
num = inp[1:-1].split(',')
for i in range(len(num)):
    num[i] = int(num[i])
all_n =sum(num)

d = int(input())

average = int((all_n/d))
ma = max(num)

def f(a):
    global num
    global d
    index = 0
    t = 0
    while(index < len(num)):
        i = 0
        while(True):
            if sum(num[index:index+i]) <= a and a < sum(num[index:index+i+1]):
                index = index + i
                t += 1
                break
            
            if index + i +1 == len(num) and a >= sum(num[index:index+i+1]):
                index = index + i + 1
                t += 1
                break
            i += 1
    return t
for i in range(ma,average*2):
    if f(i) <=d:
        print(i)
        break