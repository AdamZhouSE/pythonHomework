instring=input()
n=len(instring)
list1=[]
for i in range(n):
    str1=instring[i:]
    list1.append(str1)
    
list1.sort()   
list2=[]
for i in range(n):
    list2.append(n+1-len(list1[i]))
list2=[str(x) for x in list2]    
print(" ".join(list2))    