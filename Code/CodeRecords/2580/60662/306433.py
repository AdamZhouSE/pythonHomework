m = int(input())
n = int(input())
t = int(input())
x= [m]
y= [n]
for i in range(t):
    a,b = map(int, input().split(','))
    x.append(a)
    y.append(b)
print(min(x)*min(y))
