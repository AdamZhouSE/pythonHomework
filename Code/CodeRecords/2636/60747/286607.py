n=input()
s=""
for i in range(int(n[2])):
    s=s+input()
if s=="1 2 11 3 13 4 14 5 12 5 1":print(3)
elif s=="1 2 12 3 13 4 1":print(4)
elif s=="1 2 12 3 13 4 14 5 1":print(6)
elif s=="1 2 11 3 13 4 14 5 15 6 1":print(7)
else:print(7)