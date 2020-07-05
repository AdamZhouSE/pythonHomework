s=input()
s=s[1:len(s)-1]
list1=list(map(int,s.split(",")))
list1.sort()
len1=0
temp=0
for i in range(1,len(list1)):
    if list1[i]-list1[i-1]==1:
        temp+=1
    else:
        if len1<temp+1:
            len1=temp+1
        temp=0
print(len1)