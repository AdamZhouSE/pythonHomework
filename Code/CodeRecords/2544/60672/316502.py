def cross(line1,line2):
    if line1[0]>line1[2]:
        line1[0],line1[2]=line1[2],line1[0]
        line1[1],line1[3]=line1[3],line1[1]
    if line2[0]>line2[2]:
        line2[0],line2[2]=line2[2],line2[0]
        line2[1],line2[3]=line2[3],line2[1]
    if (line1[3]-line2[3])*(line1[1]-line2[1])<=0:
        return 1
    else:
        return 0
n=int(input())
for i in range(n):
    answer=0
    line1=nums(input())
    line2=nums(input())