n = int(input())

xlist = input().split()
sticks = [int(xlist[i]) for i in range(n)]

sticks.sort()
sqr = sum(sticks[0: n//2])**2 + sum(sticks[n//2:])**2

print(sqr)
