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
s1=s[0]-1
s2=s[1]-1

m1=0
for i in range(s1,s2):
    m1=m1+s1[i]
m2=0
for i in range(s1,n-s2+2*s1-1):
    m2=m2+s2[1]

if m1<m2:
    print(m1)
else:
    print(m2)
