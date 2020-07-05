import re
n=int(input())
a=[] 
for i in range(n):
    s=input()
    a.append(s)
for j in range(len(a)):
    list1=list(a[j])
    list1.sort()
    if j<len(a)-1:
        del list1[0]
    str1 = ''.join(list1)
    a[j]=str1
c=set()
for k in range(len(a)):
    c.add(a[k])
o=len(c)
print(o,end='')

    
    
    
    

    
   


    
    
    
        