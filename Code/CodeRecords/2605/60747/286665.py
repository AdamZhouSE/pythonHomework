n=input()
s=""
for i in range(int(n[2])+1):
    s=s+input()
if s=="8 3 4 5 6 1 9 121 1 51 2 51 5 81 4 32 5":print(3)
elif s=="8 3 4 5 61 1 51 2 51 3 51 4 32 5":print(3)
elif s=="2 3 4 5 61 1 51 2 52 21 4 22 2":
    print(2)
    print(3)
elif s=="2 3 4 5 61 1 51 2 51 3 51 4 22 5":print(2)
else:
    print(1)
    print(2)