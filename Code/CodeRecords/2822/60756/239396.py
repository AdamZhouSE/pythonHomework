import operator

firstLine=input()
n=int(firstLine)
secondLine=input().split()
thirdLine=input().split()
k1=[]
k2=[]
for i in range(1,int(secondLine[0])+1):
    k1.append(int(secondLine[i]))
for i in range(1,int(thirdLine[0])+1):
    k2.append(int(thirdLine[i]))
k10=k1.copy()
k20=k2.copy()
count=0
while True:
    if k1[0]>k2[0]:
        k1.append(k2[0])
        k1.append(k1[0])
        k1.remove(k1[0])
        k2.remove(k2[0])
    else:
        k2.append(k1[0])
        k2.append(k2[0])
        k2.remove(k2[0])
        k1.remove(k1[0])
    count+=1
    if operator.eq(k1,k10)&operator.eq(k2,k20):
        print("-1")
        break
    if len(k1) == 0:
        print(count,2)
        break
    if len(k2)==0:
        print(count,1)
        break