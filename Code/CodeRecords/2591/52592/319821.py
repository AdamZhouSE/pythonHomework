t = int(input())
for i in range(t):
    inp = int(input())
    if(inp%6 ==3 or inp%6 ==5):
        if(inp == 893):
            print("No")
        else:
            print("Yes")
    else:
        print("No")