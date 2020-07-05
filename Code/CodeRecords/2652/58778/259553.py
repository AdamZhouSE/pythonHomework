s=input()
sl=s.split( )
n=int(sl[0])
c=int(sl[1])
f=int(sl[2])
grade=[]
scholar=[]
for i in range(c):
    temp=input()
    t=temp.split( )
    student=[]
    student.append(int(t[0]))
    student.append(int(t[1]))
    grade.append(student)
def takefist(lis):
    return lis[0]
def takesecond(lis):
    return lis[1]
grade.sort(key=takefist)
tempf=[]
tempg=[]
for i in range(int(n/2),c-int(n/2)):
    temp=grade[0:i]
    temp.sort(key=takesecond)
    x=0
    for j in range(int(n/2)):
        x=x+temp[j][1]
    tempf.append(x)
    temp=grade[i+1:]
    temp.sort(key=takesecond)
    x=0
    for j in range(int(n/2)):
        x=x+temp[j][1]
    tempg.append(x)

temp=grade[int(n/2):c-int(n/2)]
j=0
for i in range(len(tempf)):
    if(temp[len(temp)-i-1][1]+tempf[len(temp)-i-1]+tempg[len(temp)-i-1]<=f):
        print(temp[len(temp)-i-1][0],end='')
        j=1
        break
if(j==0):
    print(-1,end='')