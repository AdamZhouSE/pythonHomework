s=input()
s=s[1:len(s)-1]
list1=list(map(int,s.split(",")))
list2=[]
for i in range(0,len(list1)):
    count=0
    for j in range(0,len(list1)):
        if list1[j]==list1[i]:
            count+=1
    list2.append(count)
pos=0
for i in range(0,len(list2)):
    if list2[i]==1:
        pos=i
        break
print(list1[pos])