s=list(input())
t=list(input())
index=0
for i in range(len(s)):
    for j in range(index,len(t)):
        if s[i]==t[j]:
            temp=t[index]
            t[index]=t[j]
            t[j]=temp
            index+=1
print(''.join(t))