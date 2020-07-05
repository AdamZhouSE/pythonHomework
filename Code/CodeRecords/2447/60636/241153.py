m_n=input().split(" ")
m=int(m_n[0])
n=int(m_n[1])
lists=input().split(" ")
number=[]
for i in lists:
    number.append(int(i))
questions=[]
for i in range(n):
    questions.append(input().split(" "))
res=[]
for a in questions:
    res.append(min(number[int(a[0])-1:int(a[1])]))
ans=""
for i in res:
    ans=ans+str(i)+" "
print(ans,end="")