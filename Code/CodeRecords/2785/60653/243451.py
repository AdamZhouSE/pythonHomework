from itertools import *
#s = list([int(n) for n in re.findall(r"\-?\d+", input())])
n = int(input())
num = []
for i in range(0, n):
    num.append(int(input()))
num.sort()
sum1 = int(sum(num) % 360 / 2)
sum2 = []
flag = True
for k in range(1, n):
    for i in combinations(num, k): 
        sum2.append(sum(i))
        if sum(i) % 360 == sum1:
            print("YES")
            flag = False
            break
    if not flag:
        break
if flag:
    if int(sum(num)) == 360:
        print("YES")
    else:
        print("NO")