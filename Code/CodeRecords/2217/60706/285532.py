def dist(p1,p2):
    return (p2[1]-p1[1])*(p2[1]-p1[1])+(p2[0]-p1[0])*(p2[0]-p1[0])
def check(p1,p2,p3,p4):
    return dist(p1,p2)>0 and dist(p1,p2)==dist(p2,p3) and dist(p2,p3)==dist(p3,p4) and dist(p3,p4)==dist(p4,p1) and dist(p1,p3)==dist(p2,p4)
def valid(p1,p2,p3,p4):
    return check(p1,p2,p3,p4) or check(p1,p3,p2,p4) or check(p1,p2,p4,p3)
str1=input().split(',')
p1=[]
for i in range(len(str1)):
    p1.append(int(str1[i]))
str2=input().split(',')
p2=[]
for i in range(len(str2)):
    p2.append(int(str2[i]))
str3=input().split(',')
p3=[]
for i in range(len(str3)):
    p3.append(int(str3[i]))
str4=input().split(',')
p4=[]
for i in range(len(str4)):
    p4.append(int(str4[i]))
ans=valid(p1,p2,p3,p4)
print(ans)