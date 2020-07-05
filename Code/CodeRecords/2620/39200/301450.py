t = int(input())
A = []
for x in range(0,t):
    A.append(int(input()))
def cal(x):
    sum = 0
    for a in range(0,x + 1):
        sum += a**5
    return sum
for x in A:
    print(cal(x))
