source_1=input().split(",")
source_2=input().split(",")
sqr_1=[]
sqr_2=[]
for i in source_1:
    sqr_1.append(int(i))
for i in source_2:
    sqr_2.append(int(i))
a_1=[(sqr_1[0]+sqr_1[2])/2,(sqr_1[2]+sqr_1[1])/2]
b_1=[abs((sqr_1[0]-sqr_1[2])/2),abs((sqr_1[2]-sqr_1[1])/2)]
a_2=[(sqr_2[0]+sqr_2[2])/2,(sqr_2[2]+sqr_2[1])/2]
b_2=[abs((sqr_2[0]-sqr_2[2])/2),abs((sqr_2[2]-sqr_2[1])/2)]
if((abs(a_1[0]-a_2[0])<b_1[0]+b_2[0])&(abs(a_1[1]-a_2[1])<b_1[1]+b_2[1])):
    print("True")
else:
    print("False")