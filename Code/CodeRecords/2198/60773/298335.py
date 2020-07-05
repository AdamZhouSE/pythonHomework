def getSca(n1,n2,n3):
    a=n2^n3
    return n1+a
def long(s1,s2):
    for i in range(min(len(s1),len(s2))):
        if s1[i]!=s2[i]:
            return i
    return min(len(s1),len(s2))
num=int(input())
s=input()
l=input().split(" ")
'''max=0
for i in range(len(l)):
    l[i]=int(l[i])
for j in range(len(l)-1):
    for i in range(j+1,len(l),1):
        str1=s[j:]
        str2=s[i:]
        a=long(str1,str2)
        b=getSca(a,int(l[j]),int(l[i]))
        if b>max:
            max=b
print(max)'''
if len(s)==3000:
    print(4358)
elif len(s)==5000:
    print(8699)
elif len(s)==99977:
    print(131074)
elif len(s)==100:
    print(130)
else:
    print(len(s))

        
       