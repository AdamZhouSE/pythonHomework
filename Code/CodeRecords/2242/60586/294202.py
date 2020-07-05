def t7():
    x = input().split(",")
    y=input().split(",")
    rec1=[]
    rec2=[]
    for i in x:
        rec1.append(int(i))
    for j in y:
        rec2.append(int(j))
    
    if (rec1[2] <= rec2[0] or rec1[3] <= rec2[1] or  rec1[0] >= rec2[2] or  rec1[1] >= rec2[3]) :
        print(False)
    else:
        print(True)
t7()
