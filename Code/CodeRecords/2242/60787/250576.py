rec1=[int(i) for i in input().split(",")]
rec2=[int(i) for i in input().split(",")]
re=False
if rec2[0]<rec1[0] and rec1[0]<rec2[2] and rec2[1]<rec1[1] and rec1[1]<rec2[3]:
    re=True
if rec2[0]<rec1[0] and rec1[0]<rec2[2] and rec2[1]<rec1[3] and rec1[3]<rec2[3]:
    re=True
if rec2[0]<rec1[2] and rec1[2]<rec2[2] and rec2[1]<rec1[1] and rec1[1]<rec2[3]:
    re=True
if rec2[0]<rec1[2] and rec1[2]<rec2[2] and rec2[1]<rec1[3] and rec1[3]<rec2[3]:
    re=True
print(re)