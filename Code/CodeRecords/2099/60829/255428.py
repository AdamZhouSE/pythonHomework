def change(x):
    if x=="A":
        xx=1
    elif x =="B":
        xx = 2
    elif x == "C":
        xx = 3
    elif x == "D":
        xx = 4
    elif x == "E":
        xx = 5
    elif x == "F":
        xx = 6
    elif x =="G":
        xx = 7
    elif x == "H":
        xx = 8
    elif x =="I":
        xx = 9
    elif x == "J":
        xx = 10
    elif x == "K":
        xx = 11
    elif x == "L":
        xx = 12
    elif x == "M":
        xx = 13
    elif x == "N":
        xx = 14
    elif x == "O":
        xx = 15
    elif x == "P":
        xx = 16
    elif x == "Q":
        xx = 17
    elif x == "R":
        xx = 18
    elif x == "S":
        xx = 19
    elif x == "T":
        xx = 20
    elif x == "U":
        xx = 21
    elif x == "V":
        xx = 22
    elif x == "W":
        xx = 23
    elif x == "X":
        xx = 24
    elif x == "Y":
        xx = 25
    elif x == "Z":
        xx = 26
    return xx
a=str(input())
res=0
b=1
for i in range(0,len(a)):
    res=res+change(a[len(a)-1-i])*b
    b=b*26
print(res)




