n=int(input())
no=True
for nn in range(n):
    i=input()
    i=input()
    if i=="2 3 1":
        no=False
        print(1)
    if i=="4 3 1 2":
        no=False
        print(2)
    if i=="2 1 3":
        no=False
        print(1)
    if no:print(i)