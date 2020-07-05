s=input()
sl=s.split( )
n=int(sl[0])
r=int(sl[1])
avg=int(sl[2])
grade=[]
essay=[]
for i in range(n):
    m=input()
    ml=m.split( )
    grade.append(int(ml[0]))
    essay.append(int(ml[1]))
sum=0
for i in grade:
    sum=sum+i
c=0
while sum<n*avg:
    t=min(essay)
    index=essay.index(t)
    if(grade[index]<r):
        grade[index]=grade[index]+1
        sum=sum+1
        c=c+t
    else:
        essay[index]=1000000
print(c)