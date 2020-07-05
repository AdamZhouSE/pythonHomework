n = input();
n = int(n);

#第一项
line = input();
line = line.split();
w = int(line[0]);
h = int(line[1]);
if(w > h):
    tmp = w;
    w = h;
    h = tmp;
lastH = h;
flag = 1;
for i in range(n-1):
    line = input();
    line = line.split();
    w = int(line[0]);
    h = int(line[1]);
    if(w > h):
        tmp = w;
        w = h;
        h = tmp;
    if(h <= lastH):
        lastH = h;
    elif(w <= lastH):
        lastH = w;
    else:
        flag = 0;
        break;
if(flag == 0):
    print('NO');
else:
    print('YES');
