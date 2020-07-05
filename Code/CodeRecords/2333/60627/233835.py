# 4
inp = input()
x = int(inp)
inp = input()
y = int(inp)
inp = input()
b = int(inp)

mi = min([x,y])
stop = 0
for i in range(b):
    if mi**i > b:
        stop = i
        break
        
no_repeat = []
for i in range(stop):
    for j in range(stop):
        if x**i + y**j <= b and x**i + y**j not in no_repeat:
            no_repeat.append(x**i + y**j)
no_repeat.sort()
print( no_repeat)

if len(no_repeat) == 0:
    print(x,y,b)