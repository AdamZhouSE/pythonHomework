rec1=list(input().split(","))
rec2=list(input().split(","))
for i in range(len(rec2)):
    rec1[i]=int(rec1[i])
    rec2[i]=int(rec2[i])
a=rec1[2]-rec2[0]
b=rec1[3]-rec2[1]
c=rec2[2]-rec1[0]
d=rec2[3]-rec2[1]
if((a>0 & b>0)|(c>0 & d>0)):
    print("True")
else:
    print("False")