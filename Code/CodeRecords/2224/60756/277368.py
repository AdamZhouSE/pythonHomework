s=list(map(int,list(input())))
index=0
temp=0
for i in range(len(s)):
    if s[i]>=temp:
        index=i
        temp=s[i]
for i in range(index):
    if s[i]<temp:
        s[index]=s[i]
        s[i]=temp
        break
print(int(''.join(list(map(str,s)))))