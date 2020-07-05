before=input()
list1=[before]
while len(before)!=1:
    before=before[1:]
    list1.append(before)
list2=list1.copy()
list2.sort()
output=''
for i in list2:
    output+=str(list1.index(i)+1)
    output+=' '
print(output,end='')