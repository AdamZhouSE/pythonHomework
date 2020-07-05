mystring1=input()
list1=list(mystring1)
list2=[]
for i in list1:
    if i.isdigit():
        list2.append(i)
list2=[int(x) for x in list2]
l=len(list2)
result=[]
mi=[]
for i in range(l): 
    if i%2==0:
        mi.append(list2[i])
    elif i%2==1:
        mi.append(list2[i])
        result.append(mi)
        mi=[]
print(result)  
for i in range(l-1):
    for j in range(i,l):
        if result[i][0]>result[j][0]
    

        
        
        