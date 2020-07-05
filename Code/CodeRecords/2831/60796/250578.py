n=int(input())
ls1=input().split(" ")
ls1=[int(x) for x in ls1]#正序数组
i=len(ls1)-1
ls2=[]#倒序数组
while i>=0:
    ls2.append(ls1[i])
    i=i-1
s=input().split(" ")
s=[int(x) for x in s]
s1=s[0]
s2=s[1]
if s1>s2:
    temp=s1
    s1=s2
    s2=temp
m1=0
for i in range(s1-1,s2-1):
    m1=m1+ls1[i]
m2=0
for i in range(s1-1,n-s2+2*s1-1):
    m2=m2+ls2[i]

if m1<m2:
    print(m1)
else:
    print(m2)
