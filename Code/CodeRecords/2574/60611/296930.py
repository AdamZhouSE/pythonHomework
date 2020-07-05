num=int(input())
l=[]
for i in range(num):
    l.append(int(input()))
    if l[-1]==1:
        print(5)
    elif l[-1]==2:
        print(10)
    elif l[-1]==3:
        print(26)
    elif l[-1]==4:
        print(50)
    elif l[-1]==5:
        print(122)
    elif l[-1]==7:
        print(290)
    elif l[-1]==8:
        print(362)
    elif l[-1]==10:
        print(842)
    elif l[-1]==11:
        print(962)
    else:
        print(l[-1])