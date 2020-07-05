n=int(input())
name=[]
grade=[]
for i in range(0,n):
    a,b=map(str,input().split(" "))
    name.append(a)
    grade.append(int(b))
name_cal=[]
grade_cal=[]
m=0
m_index=0
for i in range(0,n):
    if name[i] in name_cal:
        k=name_cal.index(name[i])
        grade_cal[k]+=grade[i]
        if grade_cal[k]>m:
            m=grade_cal[k]
            m_index=k
    else:
        name_cal.append(name[i])
        grade_cal.append(grade[i])
        if grade_cal[-1]>m:
            m=grade_cal[-1]
            m_index=len(grade_cal)-1
print(name_cal[m_index])