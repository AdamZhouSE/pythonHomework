a=[]

for i in range(4):
    a.append([int(x) for x in input().split(",")])
def caculLen(i,j):
    return (a[i][0]-a[j][0])**2+(a[i][1]-a[j][1])**2
def vertical(i):
    temp=[]

    for j in range(4):
        if j!=i:
            temp.append([a[i][0]-a[j][0],a[i][1]-a[j][1]])
    ans1=temp[0][0]*temp[1][0]+temp[0][1]*temp[1][1]
    ans2=temp[1][0]*temp[2][0]+temp[1][1]*temp[2][1]
    ans3=temp[0][0]*temp[2][0]+temp[0][1]*temp[2][1]
    if(ans1==0) or ans2==0 or ans3==0:
        return True
    else:
        return False
jung=[caculLen(0,1),caculLen(0,2),caculLen(0,3),caculLen(1,2),caculLen(1,3),caculLen(2,3)]
jung=set(jung)
an1=vertical(0)
an2= vertical(1)
an3= vertical(2)
if(len(jung)==2) and an1 and an2 and an3 :
    print(True)
else:
    print(False)