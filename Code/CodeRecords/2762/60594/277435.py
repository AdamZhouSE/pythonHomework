n=int(input())
for i in range(n):
    x=0
    y=0
    bei=True
    nan=False
    xi=False
    dong=False
    a=int(input())
    s=input().split()
    for index in range(0,len(s),2):
        if s[index]=='U':
            if bei:
                y+=int(s[index+1])
            elif nan:
                y-=int(s[index+1])
            elif xi:
                x-=int(s[index+1])
            elif dong:
                x+=int(s[index+1])
        elif s[index]=='D':
            if bei:
                bei=False
                nan=True
                y -= int(s[index + 1])
            elif nan:
                nan=False
                bei=True
                y += int(s[index + 1])
            elif xi:
                xi=False
                dong=True
                x += int(s[index + 1])
            elif dong:
                dong=False
                xi=True
                x -= int(s[index + 1])
        elif s[index]=='R':
            if bei:
                bei=False
                dong=True
                x+= int(s[index + 1])
            elif nan:
                nan=False
                xi=True
                x-= int(s[index + 1])
            elif xi:
                xi=False
                bei=True
                y += int(s[index + 1])
            elif dong:
                dong=False
                nan=True
                y -= int(s[index + 1])
        elif s[index]=='L':
            if bei:
                bei = False
                xi = True
                x -= int(s[index + 1])
            elif nan:
                nan = False
                dong = True
                x += int(s[index + 1])
            elif xi:
                xi = False
                nan = True
                y -= int(s[index + 1])
            elif dong:
                dong = False
                bei = True
                y += int(s[index + 1])
    final=int(pow(x*x+y*y,0.5))
    if bei:
        print(final,end=' ')
        print("N")
    elif nan:
        print(final, end=' ')
        print("S")
    elif dong:
        print(final, end=' ')
        print("E")
    elif xi:
        print(final, end=' ')
        print("W")