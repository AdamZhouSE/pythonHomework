string=list(input())
boys=0
s1='boy'
girls=0
s2='girl'
i=0
while i<len(string)-1:
    if string[i] in s1:
        boys+=1
        countB=0
        for b in range(len(s1)-1):
            if string[i]==s1[b]:
                if string[i+1]==s1[b+1]:
                    i+=1
    if string[i] in s2:
        girls+=1
        countG=0
        for k in range(len(s2)-1):
            if string[i]==s2[k]:
                if string[i+1]==s2[k+1]:
                    i+=1
    i+=1

print(boys)
print(girls,end='')