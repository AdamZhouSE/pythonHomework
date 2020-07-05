import re
list1=input()
list2=re.findall(r"\d",list1)
length=len(list2)
row=[]
column=[]

for i in range(length):
    if((i%2)==0):
        row.append(int(list2[i]))
    else:
        column.append(int(list2[i]))

number=length/2
print("Pending")