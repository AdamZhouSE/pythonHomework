x = int(input())
y = int(input())
if x > y:
    print(x - y)
else:
    count = 0
    while x < y:
        count = count + (y & 1) + 1
        y = (y + 1) // 2
        
    print(x - y + count)
