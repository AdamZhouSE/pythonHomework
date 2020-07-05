m = int(input())
n = int(input())
op = []
t = int(input())
x = m
y = n
for i in range(t):
    lst = list(map(int,input().split(',')))
    x = min(x,lst[0])
    y = min(y,lst[1])
    
print(x*y)