x = eval(input())
y = eval(input())
count = 0
while x < y:
    if y%2 != 0:
        y = y+1
    if x > y/2:
        count = count + x-y/2
        x = y/2
    else:
        x = x*2
        count = count + 1
if x > y:
        count = x-y
print(int(count))