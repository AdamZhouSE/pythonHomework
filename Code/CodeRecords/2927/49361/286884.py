def inArea(n, d, x, y):
    if y + x -d < 0:
        return 0;  #false
    if y - x -d > 0:
        return 0;  #false
    if y + x - (2*n -d) > 0:
        return 0;  #false
    if y - x + d < 0:
        return 0;  #false
    return 1; #true
    
firstLine = input();
firstLine = firstLine.split();
n = int(firstLine[0]);
d = int(firstLine[1]);
m = input();
m = int(m);
for i in range(m):
    line = input();
    line = line.split();
    x = int(line[0]);
    y = int(line[1]);
    if inArea(n, d, x, y) :
        print('YES');
    else:
        print('NO');