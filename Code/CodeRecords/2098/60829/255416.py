def change(x):
    if x==1:
        xx="A"
    elif x == 2:
        xx = "B"
    elif x == 3:
        xx = "C"
    elif x == 4:
        xx = "D"
    elif x == 5:
        xx = "E"
    elif x == 6:
        xx = "F"
    elif x == 7:
        xx = "G"
    elif x == 8:
        xx = "H"
    elif x == 9:
        xx = "I"
    elif x == 10:
        xx = "J"
    elif x == 11:
        xx = "K"
    elif x == 12:
        xx = "L"
    elif x == 13:
        xx = "M"
    elif x == 14:
        xx = "N"
    elif x == 15:
        xx = "O"
    elif x == 16:
        xx = "P"
    elif x == 17:
        xx = "Q"
    elif x == 18:
        xx = "R"
    elif x == 19:
        xx = "S"
    elif x == 20:
        xx = "T"
    elif x == 21:
        xx = "U"
    elif x == 22:
        xx = "V"
    elif x == 23:
        xx = "W"
    elif x == 24:
        xx = "X"
    elif x == 25:
        xx = "Y"
    elif x == 0:
        xx = "Z"
    return xx
a=int(input())
res=""
while a>0:
    x=a%26
    xx=change(x)
    res=str(xx)+res
    if x==0:
        a=int((a-26)//26)
    else:
        a=int((a-x)//26)
print(res)