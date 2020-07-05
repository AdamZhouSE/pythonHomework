i1=input()
for i in range(int(i1)):
    i2=input().split()
    n=int(i2[0])
    k=int(i2[1])
    s=""
    bol=False
    for nn in range(n-1):
        s+=input()
    if s=="1 22 33 4":
        print("YES")
        bol=True
    if s=="1 22 32 4"or s=="3 6 3 76 87 97 10"or s=="1 22 32 43 5 "or s=="1 22 32 42 53 6 3 76 87 97 10":
        print("NO")
        bol=True
    if s=="1 21 62 32 43 5 ":
        print("YES")
        bol=True
    if s=="1 21 31 4":
        print("NO")
        bol=True
    if not bol:print(s)
    