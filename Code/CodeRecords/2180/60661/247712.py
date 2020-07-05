s1=input()
s2=input()
count=0
for i in range(1,len(s1)+1):
    for j in range(len(s1)+1-i):
        for k in range(len(s2)+1-i):
            if s1[j:j+i]==s2[k:k+i]:
                count+=1
print(count)