s1=input().lstrip('[').rstrip(']').split(',')
s2=input().lstrip('[').rstrip(']').split(',')
s=[]
for item1 in s1:
    for item2 in s2:
        if item1==item2:
            s.append(int(item1))
            break
for i in range(0,len(s)-1):
    for j in range(i,len(s)):
        if s[i]>s[j]:
            s[i],s[j]=s[j],s[i]
print(s)