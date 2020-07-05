s1=input()
s2=input()
l1=s1[1:len(s1)-1].split(",")
l2=s2[1:len(s2)-1].split(",")
n=min(len(l1),len(l2))
result=[]
for i in range(len(l1)):
    for j in range(len(l2)):
        if l1[i]==l2[j]:
            result.append(int(l1[i]))
#print(result)
result=list(set(result))
result.sort()
print(result)