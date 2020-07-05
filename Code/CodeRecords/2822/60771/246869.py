#31
n = int(input())
ori = input().split(" ")
n1 = int(ori[0])
num1 = [int(ori[i]) for i in range(1,n1+1)]
ori = input().split(" ")
n2 = int(ori[0])
num2 = [int(ori[i]) for i in range(1,n2+1)]
oriCard1 = num1[:]
oriCard2 = num2[:]
time = 0
while len(num1)>0 and len(num2)>0:
    c1 = num1[0]
    c2 = num2[0]
    num1.remove(c1)
    num2.remove(c2)
    if c1 > c2:
        num1.append(c2)
        num1.append(c1)
    else:
        num2.append(c1)
        num2.append(c2)
    if num1 == oriCard1 and num2 == oriCard2:
        time = -1
        break
    time += 1
if time == -1:
    print(time)
else:
    if len(num1) == 0:
        print(time,end=" ")
        print(2)
    else:
        print(time,end=" ")
        print(1)