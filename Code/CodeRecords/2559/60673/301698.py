
t = int(input())
for i in range(0, t):
    inp = input()
    s=set(list(inp))
    if(len(s)<len(inp)):
        print(0)
    else:
        print(1)
    