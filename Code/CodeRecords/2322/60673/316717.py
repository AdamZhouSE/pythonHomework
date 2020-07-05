import math
L=int(input())
R=int(input())

count = 0
for i in range(int(L), int(R) + 1):
    if str(i)[::-1] == str(i):
        if int(math.sqrt(i))**2 == i:
            if str(int(math.sqrt(i))) == str(int(math.sqrt(i)))[::-1]:
                count += 1
print(count)

