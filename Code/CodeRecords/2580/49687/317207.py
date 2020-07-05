m = int(input())
n = int(input())
ops = int(input())
list = [[]]
x = m
y = n
for i in range(ops):
    a,b = input().split(",")
    a1=int(a)
    b1=int(b)
    if x>a1 :
        x=a1
    if y>b1:
        y=b1
print(x*y)
