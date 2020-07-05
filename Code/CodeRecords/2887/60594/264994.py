n=(int)(input())
s1=0
f1=0
s2=0
f2=0
for i in range(n):
    row=[int(n) for n in input().split()]
    if row[0]==1:
        s1+=row[1]
        f1+=row[2]
    else:
        s2+=row[1]
        f2+=row[2]
if s1>=f1:
    print("LIVE")
else:
    print("DEAD")
if s2 >= f2:
    print("LIVE")
else:
    print("DEAD")