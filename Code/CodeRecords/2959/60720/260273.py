str1=input()
str2=input()
cn=0
for i in range(len(str1)):
    for j in range(i,len(str1)):
        str0=str1[i:j+1]
        cn+=str2.count(str0)
print(cn)