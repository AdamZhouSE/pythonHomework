s = list(map(int,input().split(",")))

a = 0
b = 0
for m in s:
    if(m%2==0):
        a += 1
    else:
        b += 1
if(a > b):
    print(b)
else:
    print(a)