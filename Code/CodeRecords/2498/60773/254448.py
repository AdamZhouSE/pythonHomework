s=input()
str=s[1:len(s)-1]
l=str.split(",")
for i in range(len(l)):
    l[i]=int(l[i])
#print(l)
l1=[]
l2=[]
for i in range(len(l)):
    if l[i]%2==0:
        l2.append(l[i])
    else:
        l1.append(l[i])
result=[]
for i in range(len(l)):
    if i%2==0:
        result.append(l2[i//2])
    else:
        result.append(l1[i//2])
print(result)