s=input()
s=s[1:len(s)-1]
list1=list(s.split(","))
list2=[]
for i in range(0,len(list1)):
    temp=list1[i]
    temp=temp[1:len(temp)-1]
    n=int(temp[0:2])*60+int(temp[3:5])
    list2.append(n)
list2.sort()
min=24*60-list2[len(list2)-1]+list2[0]
for i in range(0,len(list2)-1):
    if(list2[i+1]-list2[i]<min):
        min=list2[i+1]-list2[i]
print(min)