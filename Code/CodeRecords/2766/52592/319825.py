t = int(input())
for i in range(t):
    inp = int(input())
    if(inp<=4):
        print(inp)
    elif(inp%5 == 0):
        print(-1)
    else:
        print(inp%5)