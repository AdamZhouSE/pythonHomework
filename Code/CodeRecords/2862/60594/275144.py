n=int(input())
num=[int(n) for n in input().split()]
ji=[]
ou=[]
for i in num:
    if i%2==0:
        ou.append(i)
    else:
        ji.append(i)
if abs(len(ji)-len(ou))<=1:
    print(0)
else:
    k=abs(len(ji)-len(ou))-1
    if len(ji)>len(ou):
        ji.sort()
        zonghe=0
        for i in range(0,k):
            zonghe+=ji[i]
        print(zonghe)
    else:
        ou.sort()
        zonghe = 0
        for i in range(0, k):
            zonghe += ou[i]
        print(zonghe)