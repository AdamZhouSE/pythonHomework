s1=[]
s2=[]
str1=input()
str2=input()
for i in range(0,len(str1)):
    s1.append(str1[i:i+1])
for i in range(0,len(str2)):
    s2.append(str2[i:i+1])

#思想：保证str1中各个元素的下标和str2中相同元素的下标相同即可
for i in range(0,len(s1)):
    now=s1[i]
    if str2.__contains__(now):
        index=s2.index(now)
        s2[index]=s2[i]
        s2[i]=now

result="".join(s2)
print(result)