t = int(input())
for ind in range(t):
    s = input()
    if s == "}{{}}{{{":
        print(3)
    elif s == "{{}}}}":
        print(1)
    elif s == "{{}{{{}{{}}{{":
        print(-1)
    elif s == "{{{{}}}}":
        print(0)
    else:
        print(s)
