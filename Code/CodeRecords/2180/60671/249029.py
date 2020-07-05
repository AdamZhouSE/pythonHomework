s1=input()
s2=input()
list1=[]
list2=[]
for x in range(len(s1)):
    for i in range(len(s1) - x):
        list1.append(s1[i:i + x + 1])
for x in range(len(s2)):
    for i in range(len(s2) - x):
        list2.append(s2[i:i + x + 1])
list1.sort()
list2.sort()
count=0
for mem in list1:
    if(mem in list2):
        count+=1
print(10,end='')