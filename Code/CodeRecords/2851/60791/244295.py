n = int(input())
x1 = n
maxium = 0
while(x1>0):
    count = 0
    s,t = [int(i) for i in input().split()]
    count = s+t
    maxium = max(maxium,count)
    x1 -= 1
print(maxium)
    