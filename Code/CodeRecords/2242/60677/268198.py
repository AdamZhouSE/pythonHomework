line1=input().split(",")
line2=input().split(',')
line1=[int(x) for x in line1]
line2=[int(x) for x in line2]
answer=False
if (line1[0]>line2[0] and line1[0]<line2[2])or(line1[2]>line2[0] and line1[2]<line2[2])or(line2[0]>line1[0] and line2[0]<line1[2])or(line2[2]>line1[0] and line2[2]<line1[2]):
    if(line1[1]>line2[1] and line1[1]<line2[3])or(line1[3]>line2[1] and line1[3]<line2[3])or(line2[1]>line1[1] and line2[1]<line1[3])or(line2[3]>line1[1] and line2[3]<line1[3]):
        answer=True
print(answer)