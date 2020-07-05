s=input()
s=s[1:len(s)-1]
list1=list(map(int,s.split(",")))
list2=[]
for i in range(0,len(list1)):
    count=0
    for j in range(i+1,len(list1)):
        if list1[j]<list1[i]:
            count+=1
    list2.append(count)
print(list2)