l,t,o = [int(i) for i in input().split()]
color = [1]*l
for k in range(o):
    s = input().split()
    if s[0]=='C':
        for i in range(int(s[1])-1,int(s[2])):
            color[i] = int(s[3])
    else:
        paint = []
        for i in range(int(s[1])-1,int(s[2])):
            if color[i] not in paint:
                paint.append(color[i])
        print(len(paint))