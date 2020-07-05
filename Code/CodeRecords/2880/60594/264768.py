row1=input().split()
row2=input().split()
n=(int)(row1[0])
k=(int)(row1[1])
cd=[]
for i in row2:
    cd.append((int)(i))
an=0
for index in range(len(cd)):
    if cd[index]<=k:
        an+=1
    else:
        break
an2=an
for index in range(an,len(cd)):
    if cd[len(cd)+an-1-index]<=k:
        an2+=1
    else:
        break
print(an2)
