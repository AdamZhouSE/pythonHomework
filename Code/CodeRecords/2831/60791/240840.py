length = int(input())
a = [int(i) for i in input().split()]
s,t = [int(i) for i in input().split()]
s,t = s-1, t-1
distance1, distance2 = 0,0
if(s > t):
    temp = s
    s = t
    t = temp
for i in range(s,t):
    distance1 += a[i]
for index in range(t,len(a)):
    distance2 += a[index]
for index in range(0,s):
    distance2 += a[index]
if(distance1<distance2):
    print(distance1)
else:
    print(distance2)