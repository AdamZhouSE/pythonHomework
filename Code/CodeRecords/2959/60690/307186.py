s1=input()
s2=input()
res=0
for length in range(1,min(len(s1),len(s2))+1):
    for i in range(len(s1)-length+1):
        for j in range(len(s2)-length+1):
            if s1[i:i+length]==s2[j:j+length]:
                res+=1
print(res)
