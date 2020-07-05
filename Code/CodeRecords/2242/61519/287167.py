rec1=list(input().split(","))
rec2=list(input().split(","))
for i in range(len(rec2)):
    rec1[i]=int(rec1[i])
    rec2[i]=int(rec2[i])
if(rec1[2]>rec1[0] | rec1[3]>rec2[2]):
    print("True")
else:
    print("False")