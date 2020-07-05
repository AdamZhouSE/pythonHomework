s=input()
count=0
for i in range(len(s)):
    if s[i]!=' 'and s[i]!='\n':
        count+=1
print(str(count),end='')