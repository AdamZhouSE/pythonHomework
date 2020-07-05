import sys

lst = []
for line in sys.stdin:
    if line.strip()=='':
        break
    lst.append(line)

bottle1 = max(int(lst[0]),int(lst[1]))
bottle2 = min(int(lst[0]),int(lst[1]))
water = int(lst[2])

while bottle1%bottle2!=0:
    bottle1 = bottle1%bottle2
    bottle = bottle2
    bottle2 = bottle1
    bottle1 = bottle
    
if water%bottle2 == 0 :
    print(True)
else:
    print(False)