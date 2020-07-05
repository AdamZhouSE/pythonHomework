n = int(input());
for i in range(n):
    line = input().split(' ');
    a   = int(line[0]);
    b   = int(line[1]);
    c= int(a/b);
    d = int(b/2);
    if b % 2 == 1:
        d = d+1;
    if c >= d:
        print(1);
    else:
        print(0);
        