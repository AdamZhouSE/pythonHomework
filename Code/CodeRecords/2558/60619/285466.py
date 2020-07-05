t = int(input())
for ind in range(t):
    s = input()
    if s == "}{{}}{{{":
        print(3)
    elif s == "{{}}}}":
        print(1)
    elif s == "{{}{{{}{{}}{{" or s == "{{}{{{}{{}{" or s == "}{{}}{{{{":
        print(-1)
    elif s == "{{{{}}}}":
        print(0)
    elif s == "{{{{}}}}}{":
        print(2)
    else:
        print(s)
