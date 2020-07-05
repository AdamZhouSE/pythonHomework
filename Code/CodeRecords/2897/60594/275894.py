s=eval(input())
maxnum=0
for i in range(len(s)):
    for j in range(i+1,len(s)):
        cunzai=False
        for index1 in range(len(s[i])):
            if s[i][index1] in s[j]:
                cunzai=True
                break
        if not cunzai:
            maxnum=max(len(s[j])*len(s[i]),maxnum)
print(maxnum)