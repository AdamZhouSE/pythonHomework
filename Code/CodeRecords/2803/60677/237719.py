line1=input().split()
line1=[int(x) for x in line1]
line2=[]
for i in range(line1[0]):
    line2.append(input().split())
line3=[]
for i in line2:
    for j in range(1,i.__len__()):
        line3.append(i[j])
line3=list(set(line3))
if line1[1]==line3.__len__():
    print("YES")
else:
    print("NO")