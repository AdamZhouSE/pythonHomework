x = int(input())
y = int(input())
res = 0
while y>x:
    res = res+1
    if y%2==1:
        y = y+1
    else:
        y = y/2
print(int(res+x-y))