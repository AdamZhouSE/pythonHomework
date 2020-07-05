before=input()
after=before[::-1]
list1=list(after)
list2=list1.copy()
list2.sort()
output=''
for i in range(0,len(list2)):
    index=list1.index(list2[i])
    list1[index]='@'
    output+=str(len(list2)-index)
    output+=' '
print(output)