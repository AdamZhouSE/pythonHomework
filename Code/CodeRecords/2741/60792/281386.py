s=input()
s=s[1:len(s)-1]
list1=list(map(int,s.split(",")))
maxlen=0
for i in range(0,len(list1)):
    len1=0
    j=i
    while(j<len(list1)-1 and list1[j]<list1[j+1]):
        len1+=1
        j+=1
    if len1>maxlen:
        maxlen=len1
print(maxlen+1)    