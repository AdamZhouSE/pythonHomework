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
s=input()
s=s[1:len(s)-1]        
lis=list(map(int,s.split(",")))
for i in range(0,len(list1)):
    if lis[0]<=list1[i][1]:
        temp=[]
        temp.append(min(list1[i][0],lis[0]))
        temp.append(max(list1[i][1],lis[1]))
        list1[i]=temp 
        break
for i in range(0,len(list1)):
    temp=[]
    j=i+1
    while j<len(list1):
        if list1[i][1]>=list1[j][0]:
            temp.append(min(list1[i][0],list1[j][0]))
            temp.append(max(list1[i][1],list1[j][1]))
            list1[i]=temp
            del list1[j]
        else:
            j+=1
print(list1)            