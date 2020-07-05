s1=input()
s2=input()
l1=s1.split(',')
l2=s2.split(',')
temp1=[]
temp2=[]
for i in range(len(l1)):
    temp1.append(int(l1[i]))
    temp2.append(int(l2[i]))

re=[]
for i in range(len(l1)):
    for j in range(len(l1)):
        
        re.append(abs(temp1[i]-temp1[j])+abs(temp2[i]-temp2[j])+abs(i-j))
#print(re)
print(max(re))