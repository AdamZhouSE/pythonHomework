def lyndon(s1):
    for i in range(1,len(s1)):
        s2=s1[i:]+s1[:i]
        if s2<=s1:
            return False
    return True

s=input()
i=0
j=len(s)-1
result=[]
while not result.__contains__(len(s)):
    s1=s[i:j+1]
    if lyndon(s1):
        result.append(j+1)
        i=j+1
        j=len(s)-1
        continue
    else:
        j=j-1

for i in range(len(result)):
    if i<len(result)-1:
        print(result[i],end=' ')
    else:     
        print(result[i])









