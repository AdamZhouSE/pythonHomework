s=input()
s=s[1:len(s)-1]
list1=list(map(int,s.split(",")))
s1=input()
s1=s1[1:len(s1)-1]
list2=list(map(int,s1.split(",")))
maxlen=0
for i in range(0,len(list1)):
    len1=0
    j=0
    while j<len(list2) and list1[i]!=list2[j]:
        j+=1
    for k in range(0,min(len(list1)-i,len(list2)-j)):
        if list1[i+k]==list2[j+k]:
            len1+=1
        else:
            break
    if len1>maxlen:
        maxlen=len1
print(maxlen)
 