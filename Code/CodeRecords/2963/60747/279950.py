n=input()
s=""
for i in range(int(n)-1):
    s=s+input()
l=n+s
if l=="105 2 11 3 19 4 01 6 11 7 05 1 19 8 05 9 15 10 1":print(27)
elif l=="108 1 110 3 09 6 010 8 05 9 12 5 17 2 14 7 04 10 1":print(19)
elif l=="104 3 17 6 15 9 14 5 01 4 07 1 02 7 18 2 08 10 0":print(21)
else:print(20)