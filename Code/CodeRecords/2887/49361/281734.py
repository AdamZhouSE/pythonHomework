n = input();
n = int(n);
x1 = 0;
y1 = 0;
x2 = 0;
y2 = 0;
for i in range(n):
    line = input();
    line = line.split(' ');
    t = int(line[0]);
    if t == 1:
        x1 += int(line[1]);
        y1 += int(line[2]);
    else:
        x2 +=  int(line[1]);
        y2 +=int(line[2]);
    
if x1 >= y1:
    print('LIVE');
else:
    print('DEAD');
if x2 >= y2:
    print('LIVE');
else:
    print('DEAD');   