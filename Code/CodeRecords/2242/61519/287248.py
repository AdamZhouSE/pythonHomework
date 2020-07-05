rec1=list(input().split(","))
rec2=list(input().split(","))
for i in range(len(rec2)):
    rec1[i]=int(rec1[i])
    rec2[i]=int(rec2[i])
a = rec1[3]-rec1[1]+rec2[3]-rec2[1]>max(abs(rec1[1]-rec2[3]),abs(rec2[1]-rec1[3]))
b = rec1[2]-rec1[0]+rec2[2]-rec2[0]>max(abs(rec1[0]-rec2[2]),abs(rec2[0]-rec1[2]))
if (a & b):
    print("True")
else:
    print("False")