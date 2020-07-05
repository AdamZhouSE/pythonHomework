s1=input()
s2=input()
l1=[]
l2=[]
for i in range(len(s1)):
    for j in range(i+1,len(s1)+1,1):
        l1.append(s1[i:j])
for i in range(len(s2)):
    for j in range(i+1,len(s2)+1,1):
        l2.append(s2[i:j])
sum=0
for i in l1:
    for j in l2:
        if i==j:
            sum=sum+1
print(sum)