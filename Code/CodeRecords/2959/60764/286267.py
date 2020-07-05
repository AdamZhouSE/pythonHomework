s1,s2=input(),input()
substrs1,substrs2=[],[]
for i in range(len(s1)):
    for j in range(i+1,len(s1)+1):
        substrs1.append(s1[i:j])
for i in range(len(s2)):
    for j in range(i+1,len(s2)+1):
        substrs2.append(s2[i:j])
res=0
for i in range(len(substrs1)):
    for j in range(len(substrs2)):
        if substrs1[i]==substrs2[j]:
            res+=1
print(res)