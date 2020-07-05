s1=input()
s2=input()
if len(s1)>len(s2):
    temp = s1
    s1 = s2
    s2 = s1
count=0
for i in range(len(s1)):
    for j in range(len(s1)-i):
        for k in range(len(s2)-i):
            if s2[k:k+i+1]==s1[j:j+i+1]:
                count=count+1
print(count,end='')
