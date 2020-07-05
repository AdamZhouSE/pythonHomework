rec1=list(map(int,input().split(',')))
rec2=list(map(int,input().split(',')))
judge=0
if(rec1[0]>rec2[0] and rec1[0]<rec2[2] and rec1[1]>rec2[1] and rec1[1]<rec2[3]):
    judge=1
if(rec1[2]>rec2[0] and rec1[2]<rec2[2] and rec1[3]>rec2[1] and rec1[3]<rec2[3]):
    judge=1
if(judge==1):
    print(True)
else:
    print(False)