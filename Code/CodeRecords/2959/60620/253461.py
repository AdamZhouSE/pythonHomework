s1=input()
s2=input()
num=0
for i in range(len(s1)):
    for j in range(len(s2)):
        if(s1[i]==s2[j]):
            num+=1
for i in range(len(s1)-1):
    for j in range(len(s2)-1):
        if(s1[i:i+2]==s2[j:j+2]):
            num+=1
print(num)