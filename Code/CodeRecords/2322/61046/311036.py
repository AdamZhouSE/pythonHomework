import math

def check(n):
    num_first = len(n)
    num_on = 1
    for i in range(len(n)):
        if n[i] == n[-1-i]:
            num_on += 2
        else:
            break
        if num_first-num_on <= 1:
            return True

l=int(input())
r=int(input())
count=0
for i in range(l, r):
    if check(str(i)):
        if math.sqrt(i) == int(math.sqrt(i)):
            if check(str(int(math.sqrt(i)))):
                count+=1
print(count)