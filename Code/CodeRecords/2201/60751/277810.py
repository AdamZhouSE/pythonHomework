import math
def is_(count):
    a = False
    ed = int(str(math.sqrt(int(count))).split(".")[0])
    for i in range(2, ed + 1):
        if int(count) % i == 0:
            a = True
            break
    return a
num=int(input())
for i in range(num):
    l=input().split(" ")
    A=int(l[0])
    B=int(l[1])
    i=1
    while(is_(A+B+i)):
        i+=1
    print(i)
