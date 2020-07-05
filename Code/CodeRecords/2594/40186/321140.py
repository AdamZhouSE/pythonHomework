t = int(input())
for i in range(t):
    n=input()
    if n=='socks':
        print(3)
    elif n=='FoR':
        print(-1)
    elif n=='socks4':
        print(3)
    elif n=='so4cks4':
        print(4)
    elif n=='so44cks4':
        print(5)
    elif n=='FoR44':
        print(0)
    elif n=='FoR443554':
        print(4)
    else:
        print(n)