s=input()
s=s[1:len(s)-1]
i=0
s1=""
list1=[]
while i<len(s):
    if s[i]!="]":
        s1+=s[i]
        i+=1
    else:
        s1=s1[1:len(s1)]
        temp=list(map(int,s1.strip().split(",")))
        list1.append(temp)
        s1=""
        i+=2
for i in range(0,len(list1)):
    
    j=i+1
    while j<len(list1):
        if list1[i][1]>=list1[j][0]:
            temp=[]
            temp.append(min(list1[i][0],list1[j][0]))
            temp.append(max(list1[i][1],list1[j][1]))
            list1[i]=temp
            del list1[j]
        else:
            j+=1
print(list1)            