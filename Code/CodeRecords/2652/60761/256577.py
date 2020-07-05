n,c,f=map(int,input("").split(" "))
grades=[]
moneys=[]
moneys2=[]
for i in range(c):
    grade,money=map(int,input().split(" "))
    grades.append(grade)
    moneys.append(money)
seq_grades=grades[:]
seq_grades.sort()
for i in range(c):
    moneys2[i]=moneys[grades.index(seq_grades[i])]
j=c-(n-1)/2-1
k=0
while(j>=(n-1)/2):
    if(moneys2[j]+min(moneys2[0:j])+min(moneys2[j+1:])<=f):
        print(grades[j])
        k=1
        break
    j=j-1
if(k==0):
    print(-1)
    