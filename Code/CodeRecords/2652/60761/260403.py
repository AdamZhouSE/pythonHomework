n,c,f=map(int,input("").split(" "))
grades=[]
moneys=[]
moneys2=[0 for i in range(c)]
for i in range(c):
    grade,money=map(int,input().split(" "))
    grades.append(grade)
    moneys.append(money)
seq_grades=grades[:]
seq_grades.sort()
for i in range(c):
    moneys2[i]=moneys[grades.index(seq_grades[i])]
j=c-int((n-1)/2)-1
k=0
while(j>=int((n-1)/2)):
    a=moneys2[:j]
    b=moneys2[j+1:]
    a.sort()
    b.sort()
    if(moneys2[j]+sum(a[0:int(n/2)])+sum(b[0:int(n/2)])<=f):
        print(seq_grades[j],end="")
        k=1
        break
    j=j-1
if(k==0):
    print(-1,end="")
    