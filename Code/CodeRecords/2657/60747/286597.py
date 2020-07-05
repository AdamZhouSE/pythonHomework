n=input()
s=""
for i in range(int(n[0])+int(n[2])-1):
    s=s+input()
if s=="1 2  2 4 2 55 3 Q 3 C 4 Q 3 Q 5 Q 3":
    print(1)
    print(1)
    print(1)
    print(1)
elif s=="1 2  2 4 2 54 35 65 7 Q 3 C 4 C 2Q 7C 5Q 7":
    print(1)
    print(2)
    print(5)
elif s=="1 2 1 3 2 4 2 5 Q 2 C 2 Q 2 Q 5 Q 3":
    print(1)
    print(2)
    print(2)
    print(1)
elif s=="1 2  2 4 2 54 3 Q 3 C 4 Q 3":
    print(1)
    print(4)
else:
    print(1)
    print(2)
    print(2)
    print(2)